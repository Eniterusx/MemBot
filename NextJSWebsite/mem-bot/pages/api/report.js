import conPromise from '../../database.js'
import getSession from '../../session.js'

export default async function handler(req, res) {
  const session = await getSession(req)
  if (!session) return res.status(403).json({ error: 'Nie jesteś zalogowany.' })

  const { pictureId, reason } = req.body
  if (pictureId == null || reason == null) return res.status(400).json({ error: 'Bad request.' })
  if (typeof pictureId !== 'number' || typeof reason !== 'string') return res.status(400).json({ error: 'Bad request.' })

  const result = await conPromise('SELECT * FROM reports WHERE user_id = ? AND picture_id = ?', [session.user.user_id, pictureId]).catch(() => {})
  if (!result) return res.status(500).json({ error: 'Nie udało się sprawdzić dotychczasowych zgłoszeń.' })
  if (result[0] != null) return res.status(400).json({ error: 'Już zgłosiłeś to zdjęcie. Ogar downa.' })

  return conPromise('INSERT INTO reports (user_id, picture_id, reason_of_report) VALUES (?, ?, ?)', [session.user.user_id, pictureId, reason])
  .then(() => res.status(200).json({}))
  .catch(() => res.status(500).json({ error: 'Nie udało się zgłosić obrazka.' }))
}