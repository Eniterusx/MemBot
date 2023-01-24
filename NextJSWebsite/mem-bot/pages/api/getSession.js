import getSession from "../../session";

export default async function handler(req, res) {
  const session = await getSession(req)
  if (!session) return res.status(403).json({ error: 'Błąd walidacji sesji.' })

  return res.json({
    user_id: session.user.user_id,
    discord_id: session.user.discord_id,
    nickname: session.user.nickname,
    avatar: session.data.avatar
  })
}