// import '../styles/globals.css'

import React from 'react'
import { fetcher } from '../util'
import useSWR from 'swr'

export const SessionContext = React.createContext({
  data: null,
  mutate: () => {}
})

export default function App({ Component, pageProps }) {
  const { data: sessionData, mutate: sessionMutate } = useSWR('/api/getSession', fetcher, {
    revalidateOnFocus: false,
    revalidateOnReconnect: false
  })
  
  return (
    <SessionContext.Provider value={{ data: sessionData, mutate: sessionMutate }}>
      <Component {...pageProps} />
    </SessionContext.Provider>
  )
}
