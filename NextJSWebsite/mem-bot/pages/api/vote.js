import conPromise from '../../database.js'
import getSession from '../../session.js'

export default async function handler(req, res) {
  const session = await getSession(req)
  if (!session) return res.status(403).json({ error: 'Nie jesteś zalogowany.' })

  const { pictureId, value } = req.body
  if (pictureId == null || value == null) return res.status(400).json({ error: 'Bad request.' })
  if (typeof pictureId !== 'number' || typeof value !== 'number') return res.status(400).json({ error: 'Bad request.' })

  const voteUserValue = 1
  const voteValue = Math.sign(value) * voteUserValue

  return conPromise('REPLACE INTO votes (user_id, picture_id, vote_value) VALUES (?, ?, ?)', [session.user.user_id, pictureId, voteValue])
  .then(() => conPromise('SELECT SUM(vote_value) AS suma FROM votes WHERE picture_id = ?', [pictureId]))
  .then((result) => res.status(200).json({ suma: result[0].suma, your_vote: voteValue }))
  .catch(() => res.status(500).json({ error: 'Nie udało się zagłosować.' }))
}