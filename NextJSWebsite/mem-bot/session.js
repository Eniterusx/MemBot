import conPromise from './database'

import jwt from 'jsonwebtoken'
import { parseCookies } from 'nookies'

export default function getSession(req) {
  const cookies = parseCookies({ req })

  // Walidacja JWT
  let data
  try {
    data = jwt.verify(cookies.session, process.env.JWT_SECRET)
  } catch (e) {
    return // Błąd walidacji sesji
  }
  if (data.data.exp > Date.now() / 1000) return // Sesja wygasła

  // Wyszukujemy usera w bazie i zwracamy reszte danych
  return conPromise('SELECT * FROM users WHERE discord_id = ?', [data.data.id]).then((sqlData) => {
    const result = sqlData[0]
    if (!result) return

    return {
      data: data.data,
      user: result
    }
  }).catch(() => {})
}