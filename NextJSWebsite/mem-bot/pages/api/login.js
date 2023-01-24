import conPromise from '../../database'
import { getDiscordRedirectURI, scopes } from '../../discord'

import axios from 'axios'
import jwt from 'jsonwebtoken'
import { setCookie } from 'nookies'

const session_exp = 7 * 24 * 60 * 60000

export default async function handler(req, res) {
  const code = req.query.code
  // Brak kodu - redirect na strone glowna
  if (!code) return res.redirect('/')

  // Konstruujemy request do Discorda by zautoryzowac uzytkownika
  const data = new URLSearchParams({
    client_id: process.env.NEXT_PUBLIC_DISCORD_CLIENTID,
    client_secret: process.env.DISCORD_CLIENTSECRET,
    code: code,
    grant_type: 'authorization_code',
    redirect_uri: getDiscordRedirectURI(),
    scope: scopes.join(' ')
  })

  const result = await axios.post('https://discord.com/api/oauth2/token', data.toString()).catch(() => {})
  // Nie udało się zautoryzować użytkownika - redirect na strone glowna
  if (!result) return res.redirect('/')

  // Pobierzmy dane uzytkownika ~~i przeslijmy do Chin (moze tam serwery AGH by je utrzymały)~~
  const userResult = await axios.get('https://discord.com/api/users/@me', {
    headers: {
      Authorization: `${result.data.token_type} ${result.data.access_token}`
    }
  }).catch(() => {})
  // Moskwa zawiesiła połączenie, nie udało się pobrać danych użytkownika - redirect na strone glowna
  if (!userResult) return res.redirect('/')

  // ~~Ukradnij dane karty kredytowej uzytkownika~~
  // Nabij uzytkownikowi sesje w bazie danych / jwt
  // Ale najlepiej stworzyc osobna baze danych w AGH, zeby sie zmiescilo

  // Wrzucamy do bazy danych
  const id = userResult.data.id
  const name = `${userResult.data.username}#${userResult.data.discriminator}`
  return conPromise(`INSERT INTO users (discord_id, nickname) VALUES (?, ?)
    ON DUPLICATE KEY UPDATE discord_id = ?, nickname = ?`, [id, name, id, name]).then((sqlData) => {
      // Generujemy sesje w JWT
      const jwtCookie = jwt.sign({
        exp: Math.floor((Date.now() + session_exp) / 1000),
        data: {
          id: id,
          avatar: `https://cdn.discordapp.com/avatars/${id}/${userResult.data.avatar}.png`
        }
      }, process.env.JWT_SECRET)

      // Ustawiamy w ciastkach
      setCookie({ res }, 'session', jwtCookie, {
        maxAge: session_exp / 1000,
        path: '/'
      })
      
      return res.redirect('/')
  }).catch(() => res.redirect('/'))
}