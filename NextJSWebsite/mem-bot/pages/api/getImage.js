import conPromise from '../../database'
import getSession from '../../session'

const limitPoczekalnia = 3
export default async function handler(req, res) {
  const czyPoczekalnia = req.query.poczekalnia != null

  const sessionData = await getSession(req)
  
  return conPromise(`SELECT * FROM pictures AS p 
                    INNER JOIN (
                        SELECT p.picture_id, COALESCE(SUM(v.vote_value), 0) AS suma FROM pictures AS p
                            LEFT JOIN votes AS v USING(picture_id)
                        GROUP BY p.picture_id
                    ) AS s USING(picture_id)
                    WHERE s.suma ${czyPoczekalnia ? '<' : '>='} ? GROUP BY picture_id
                    ORDER BY RAND() 
                    LIMIT 2`, [limitPoczekalnia]).then(async (response) => {
    // Jeżeli użytkownik jest zalogowany
    if (sessionData) {
      // Dla każdego obrazka pobieramy dane o glosie
      for (const picture of response) {
        const vote = await conPromise(`SELECT * FROM votes WHERE picture_id = ? AND user_id = ?`, [picture.picture_id, sessionData.user.user_id]).catch(() => {})
        if (vote) picture.vote = { value: vote[0]?.vote_value }
      }
    }
    // Zwracamy dane
    return res.status(200).json({
      data: response.map((dane) => ({ // Sanitize lolz
        file_name: dane.file_name,
        file_type: dane.file_type,
        url: dane.url,
        picture_id: dane.picture_id,
        suma: dane.suma,
        vote: dane.vote // Jezeli uzytkownik nie jest zalogowany to null, inaczej { value: wartosc [wartosc bedzie null jesli nie glosowal] }
      }))
    })
  }).catch(err => {
    return res.status(500).json({ error: 'Nie udało się pobrać zdjęcia.' })
  })
}