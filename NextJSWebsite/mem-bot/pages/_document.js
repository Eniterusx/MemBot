import { Html, Head, Main, NextScript } from 'next/document'

const styling = {
  background: `fixed no-repeat center/101% url(/background.png)`
}


export default function Document() {
  return (
    <Html lang="en">
      <Head>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <body style={styling}>
        <Main />
        <NextScript />
      </body>
    </Html>
  )
}
