export const scopes = ['identify', 'email']

export function getDiscordRedirectURI() {
  return `${process.env.NEXT_PUBLIC_URL}/api/login`
}

export function generateDiscordLoginURL() {
  const params = new URLSearchParams({
    client_id: process.env.NEXT_PUBLIC_DISCORD_CLIENTID,
    redirect_uri: getDiscordRedirectURI(),
    response_type: 'code',
    scope: scopes.join(' ')
  })
  return `https://discord.com/api/oauth2/authorize?${params.toString()}`
}
