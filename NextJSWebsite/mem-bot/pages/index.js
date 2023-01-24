import Head from 'next/head'
import { Skeleton, Button, Typography, Grid, Card, CardHeader, CardMedia, CardActions, IconButton } from '@mui/material'
import React from 'react'

import ThumbUpAltIcon from '@mui/icons-material/ThumbUpAlt'
import ThumbUpOffAltIcon from '@mui/icons-material/ThumbUpOffAlt'
import ThumbDownAltIcon from '@mui/icons-material/ThumbDownAlt'
import ThumbDownOffAltIcon from '@mui/icons-material/ThumbDownOffAlt'
import WarningAmberOutlinedIcon from '@mui/icons-material/WarningAmberOutlined'

import ReportZdjecia from '../components/ReportZdjecia'
import DaneUzytkownika from '../components/DaneUzytkownika'
import DodawanieZdjecia from '../components/DodawanieZdjecia'
import { fetcher } from '../util'

import useSWR from 'swr'
import axios from 'axios'

import { SessionContext } from './_app.js'

export default function Home() {
  const [czyPoczekalnia, setPoczekalnia] = React.useState(false)

  // Pobieranie zdjecia z API
  const { data, mutate } = useSWR(`/api/getImage${czyPoczekalnia ? '?poczekalnia=1' : ''}`, fetcher, {
    revalidateOnFocus: false,
    revalidateOnReconnect: false
  })

  const [dodawanieOtwarte, setDodawanieOtwarte] = React.useState(false) // Czy modal dodawania plikow jest otwarty
  
  const { data: sessionData } = React.useContext(SessionContext)
  const czyZalogowano = sessionData?.user_id != null

  // Obliczanie obecnie wyswietlanego zdjecia
  const [ostatnioWyswietlone, setOstatnioWyswietlone] = React.useState()
  let obecnieWyswietlane
  if (data && data.data) {
    // Znajdz id innego zdjecia niz wyswietlone przed zmiana
    obecnieWyswietlane = data.data.find((zdjecie) => zdjecie.picture_id !== ostatnioWyswietlone)
  }
  const zmien = () => { // Zmiana zdjecia
    setOstatnioWyswietlone(obecnieWyswietlane?.picture_id) // Zapisujemy ostatnio pokazany, by sie nie zduplikowal po odswiezeniu
    mutate({}) // Odswiezamy
  }
  const zmienPoczekalnia = () => {
    setPoczekalnia((v) => !v)
    mutate({})
  }

  const [voting, setVoting] = React.useState(false)
  const vote = async (value) => {
    if (!voting) {
      setVoting(true)
      const dane = await axios.post('/api/vote', { pictureId: obecnieWyswietlane?.picture_id, value: value }, { headers: {} })
        .catch((error) => Object.assign({ error: false }, error.response.data)) // Fallback bledu - jezeli nie podano dokladnej tresci bledu - bedzie false, inaczej tekst bledu

      if (dane && dane.error == null) {
        obecnieWyswietlane.vote.value = dane.data.your_vote
        obecnieWyswietlane.suma = dane.data.suma
      } else {
        // Handling bledu
      }

      setVoting(false)
    }
  }

  const [reporting, setReporting] = React.useState() // Przechowuje dane reportowanego zdjecia

  return (
    <>
      <Head>
        <title>MemeBot</title>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </Head>
      <main>

        {/* Przyciski */}
        <Grid container sx={{ marginTop: 5 }} wrap='nowrap' alignItems='center'>
          <Grid item sm={6} sx = {{ textAlign: 'left' }}>
            <Button style={{boxShadow: '10px 10px 10px #000000'}} elevation={3} sx={{ ml: '35%', mr: 2 }} variant='contained' onClick={zmien}>Odśwież</Button>
            {(czyZalogowano) ? <Button style={{boxShadow: '10px 10px 10px #000000'}} elevation={3} sx={{ mx: 2 }} variant='contained' onClick={() => setDodawanieOtwarte(true)}>Dodaj zdjęcie</Button> : []}
          </Grid>
          <Grid item sm={6} sx={{ textAlign: 'right' }} alignItems='center'>
            <Button style={{boxShadow: '10px 10px 10px #000000', display: 'inline-flex'}} elevation={3} sx={{ mx: 2 }} variant='contained' onClick={zmienPoczekalnia}>
              {czyPoczekalnia ? 'Poczekalnia' : 'Główna'}
            </Button>
            <DaneUzytkownika/>
          </Grid>
        </Grid>

        {/* Wyświetlanie mema */}
        <Grid container alignItems='center' justifyContent='center' sx={{ marginTop: 5 }}>
          <Grid item xs={5}>
            <Card>
              {
                (obecnieWyswietlane)
                ? <>
                  <CardHeader
                    title={obecnieWyswietlane.file_name}
                    subheader={`ID: ${obecnieWyswietlane.picture_id}`}
                  />
                  <CardMedia
                    component={obecnieWyswietlane.file_type.startsWith('video') ? 'video' : 'img'}
                    src={obecnieWyswietlane.url}
                    style={{ }}
                    controls={obecnieWyswietlane.file_type.startsWith('video')}
                  />
                  <CardActions disableSpacing>
                  <Grid container>
                    <Grid item sm={6} sx = {{ textAlign: 'left' }}>
                      <IconButton onClick={() => vote(1)} disabled={!czyZalogowano || voting}>
                        {(obecnieWyswietlane.vote?.value > 0) ? <ThumbUpAltIcon /> : <ThumbUpOffAltIcon />}
                      </IconButton>
                      <Typography display="inline" sx={{ mx: 0.5 }}>
                        {obecnieWyswietlane.suma}
                      </Typography>
                      <IconButton onClick={() => vote(-1)} disabled={!czyZalogowano || voting}>
                        {(obecnieWyswietlane.vote?.value < 0) ? <ThumbDownAltIcon /> : <ThumbDownOffAltIcon />}
                      </IconButton>
                    </Grid>
                    <Grid item sm={6} sx={{ textAlign: 'right' }}>
                      <IconButton onClick={() => setReporting({ id: obecnieWyswietlane.picture_id, name: obecnieWyswietlane.file_name })} disabled={!czyZalogowano}>
                        <WarningAmberOutlinedIcon />
                      </IconButton>
                    </Grid>
                  </Grid>
                  </CardActions>
                  </>
                : <Skeleton sx={{ align: 'center' }} variant='rectangular' animation="wave" width='100%' height='500px' />
              }
            </Card>
          </Grid>
        </Grid>
        
        {/* Dodawanie zdjecia */}  
        <DodawanieZdjecia
          open={dodawanieOtwarte}
          onClose={() => setDodawanieOtwarte(false)}
        />

        {/* Reportowanie zdjecia */}
        <ReportZdjecia
          id={reporting?.id}
          name={reporting?.name}
          onClose={() => setReporting()}
        />
      </main>
    </>
  )
}
