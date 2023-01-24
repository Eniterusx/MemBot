import { Skeleton, Button, Modal, List, ListItem, Typography, Grid, Box, TextField, CircularProgress, Alert, Card, CardHeader, CardMedia, CardActions, IconButton } from '@mui/material'
import { AspectRatio } from '@mui/joy'
import Dropzone from 'react-dropzone'
import React from 'react'
import axios from 'axios'

import { akceptowaneTypy, czyBladNazwy, czyBladWielkosci } from '../util'
import ModalBox from './ModalBox'

export default function DodawanieZdjecia(props) {
  const [dodanePliki, setDodanePliki] = React.useState([]) // Dodane pliki

  // Sprawdz plik (nazwa i wielksoc)
  const sprawdzPlik = (plik) => plik.error = czyBladWielkosci(plik) ?? czyBladNazwy(plik.name)
  // Przy dodaniu pliku
  const onDrop = (files) => {
    for (const file of files) {
      const nazwaBezKropki = file.name.substr(0, file.name.lastIndexOf('.')).replaceAll('.', ' ')
      const id = Date.now().toString()
      const plik = {
        id: id,
        name: nazwaBezKropki,
        path: file.path,
        type: file.type,
        data: undefined, // Data zostanie dodane po wczytaniu pliku, dopoki nie ma - wyswietla jako loading
        error: undefined,
        readerror: false
      }
      sprawdzPlik(plik) // Sprawdz nazwe i wielkosc pliku
      dodanePliki.push(plik) // Dodajemy kazdy plik do tablicy z plikami

      // Wczytujemy plik z dysku przez API przegladarki
      const reader = new FileReader()
      reader.onload = (e) => { // Po wczytaniu
        // Aktualizujemy data po zaladowaniu o ile plik nie zostal usuniety
        setDodanePliki((pliki) => {
          const cplik = pliki.find((c) => c.id === id)
          if (cplik) {
            cplik.data = e.target.result
            sprawdzPlik(cplik) // Sprawdz ponownie po zaladowaniu pliku
          }
          return pliki
        })
      }
      reader.onerror = () => { // Przy bledzie wczytywania
        // Dodajemy blad do pliku
        setDodanePliki((pliki) => {
          const cplik = pliki.find((c) => c.id === id)
          if (cplik) {
            cplik.readerror = true // Nie udalo sie wczytac pliku
            sprawdzPlik(cplik) // Zaaktualizuj wiadomosc
          }
          return pliki
        })
      }
      reader.readAsDataURL(files[0]) // Wczytaj plik jako data URL
    }
  }
  // Funkcja do usuwania pliku
  const usunPlik = (id) => setDodanePliki((pliki) => pliki.filter((c) => c.id !== id))
  // Funkcja do zmiany nazwy pliku
  const zmienNazwe = (id, nazwa) => {
    setDodanePliki((pliki) => {
      // Znalezienie pliku
      const cplik = pliki.find((c) => c.id === id)
      if (cplik) {
        cplik.name = nazwa // Zmiana nazwy
        sprawdzPlik(cplik) // Walidacja poprawnosci
      }
      
      return [...pliki]
    })
  }

  const [uploadMessage, setUploadMessage] = React.useState() // Wiadomosc z uploadowania plikow
  const [uploading, setUploading] = React.useState(false) // Status uploadowania plikow
  // Funkcja do uploadowania plikow
  const upload = async () => {
    if (!uploading) {
      setUploading(true)
      // Upload do API
      const dane = await axios.post('/api/uploadImage', dodanePliki, { headers: {} })
        .catch((error) => Object.assign({ error: false }, error.response.data)) // Fallback bledu - jezeli nie podano dokladnej tresci bledu - bedzie false, inaczej tekst bledu

      if (dane && dane.error == null) { // Jezeli nie wystapil blad
        setDodanePliki([])
        setUploadMessage({ severity: 'success', message: 'Dodano pliki!' })
      } else { // Wyswietlenie informacji o bledzie
        setUploadMessage({ severity: 'error', message: dane.error ?? 'Nie udało się dodać plików.' })
      }
      
      setUploading(false)
    }
  }

  const zamknijUpload = () => { // Zamknij modal upoadu
    props.onClose()
    setUploadMessage()
  }

  return (<Modal
    open={props.open}
    onClose={zamknijUpload}
    closeAfterTransition
  >
    <ModalBox style={{ overflowY: 'auto', maxHeight: 'calc(200vh - 210px)' }}>
      {/* Wiadomosc z uploadowania plikow */}
      {
        uploadMessage
        ? <>
          <Alert severity={uploadMessage.severity}>{uploadMessage.message}</Alert>
          <br />
        </>
        : []
      }
      {/* Dropzone do uploadowania plikow */}
      <Dropzone onDrop={onDrop} multiple={true} accept={akceptowaneTypy}>
        {(({ getRootProps, getInputProps }) => (
          <section>
            {/* Czesc dropzone */}
            <div {...getRootProps({ className: "dropzone" })}>
              <input {...getInputProps()} />
              <Typography sx={{ color: 'blue', textDecoration: 'underline', textAlign:'center' }}>Kliknij tutaj lub przeciągnij pliki, aby je dodać.</Typography>
            </div>
            <br />
            {/* Lista dodanych plikow */}
            <aside className="selected-file-wrapper">
              <List>
                {
                  dodanePliki.map((plik, i) => {
                    return (
                      <ListItem key={i}>
                        <Grid container>
                          {/* Podglad pliku */}
                          <Grid item xs={3}>
                            <AspectRatio ratio="1/1">
                              {
                                (!plik.data)
                                  ? <Skeleton variant='rectangular' animation='wave' sx={{ width: '100%', height: '100%' }} />
                                  : (plik.type.startsWith('video'))
                                    ? <video key={i} height='100%' width='auto' controls><source src={plik.data} type={plik.type} /></video>
                                    : <img key={i} height='100%' width='auto' src={plik.data} />
                              }
                            </AspectRatio>
                          </Grid>
                          <Grid item xs={1} />
                          {/* Dane pliku i zarzadzanie */}
                          <Grid item xs={8}>
                              <TextField
                                error={plik.error != null}
                                helperText={plik.error}
                                sx={{ width: '100%' }}
                                variant='filled'
                                label='Nazwa'
                                value={plik.name}
                                onChange={(e) => zmienNazwe(plik.id, e.target.value)}
                              />

                              <Box sx={{ marginTop: 3, textAlign: 'center' }}>
                                <Button onClick={() => usunPlik(plik.id)} variant='contained'>Usuń</Button>
                              </Box>
                          </Grid>
                        </Grid>
                      </ListItem>
                    )
                  })
                }
              </List>
              {/* Przycisk uploadu */}
              <Box sx={{ textAlign: 'center' }}>
                {
                  uploading
                  ? <Button variant='contained' disabled startIcon={<CircularProgress size={20} />}>Dodaj</Button>
                  : <Button variant='contained' disabled={(dodanePliki.length == 0) || !(dodanePliki.every((plik) => plik.error == null))} onClick={upload}>Dodaj</Button>
                }
              </Box>
            </aside>
          </section>
        ))}
      </Dropzone>
    </ModalBox>
  </Modal>
  )
}