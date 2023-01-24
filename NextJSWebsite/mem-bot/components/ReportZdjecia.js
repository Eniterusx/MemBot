import { Modal, Alert, TextField, Box, Button, Typography, CircularProgress } from '@mui/material'
import React from 'react'
import axios from 'axios'
import { czyBladReportu } from '../util'

import ModalBox from './ModalBox'

export default function ReportowanieZdjecia(props) {
  const [reportMessage, setReportMessage] = React.useState() // Wiadomosc z reportowania plikow
  const [reporting, setReporting] = React.useState(false) // Status reportowania plikow

  const [zgloszono, setZgloszono] = React.useState(false)

  const [powod, setPowod] = React.useState('')

  const zamknijReport = () => { // Zamknij modal reportu
    props.onClose()
    setReportMessage()
    setPowod('')
    setZgloszono(false)
  }
  // Funkcja do reportowania plikow
  const report = async () => {
    if (!reporting) {
      setReporting(true)
      // Upload do API
      const dane = await axios.post('/api/report', { pictureId: props.id, reason: powod }, { headers: {} })
        .catch((error) => Object.assign({ error: false }, error.response.data)) // Fallback bledu - jezeli nie podano dokladnej tresci bledu - bedzie false, inaczej tekst bledu

      if (dane && dane.error == null) { // Jezeli nie wystapil blad
        setReportMessage({ severity: 'success', message: 'Zgłoszono!' })
        setZgloszono(true)
      } else { // Wyswietlenie informacji o bledzie
        setReportMessage({ severity: 'error', message: dane.error ?? 'Nie udało się zgłosić zdjęcia.' })
      }
      
      setReporting(false)
    }
  }

  const bladPowodu = czyBladReportu(powod)
  return (<Modal
    open={props.id != null}
    onClose={zamknijReport}
    closeAfterTransition
  >
    <ModalBox style={{ overflowY: 'auto', maxHeight: 'calc(200vh - 210px)' }}>
      {/* Wiadomosc z reportowania plikow */}
      {
        reportMessage
        ? <>
          <Alert severity={reportMessage.severity}>{reportMessage.message}</Alert>
          <br />
        </>
        : []
      }
      {
        (!zgloszono)
          ? (
            <>
              <Typography variant='h5' sx={{ textAlign: 'center' }}>
                Zgłaszasz zdjęcie o nazwie "{props.name}" (ID {props.id})
              </Typography>
              <br />
              {/* Textbox do repo plikow */}
              <TextField
                error={bladPowodu != null}
                helperText={bladPowodu}
                sx={{ width: '100%' }}
                variant='filled'
                label='Powód zgłoszenia'
                value={powod}
                onChange={(e) => setPowod(e.target.value)}
              />
              
              <Box sx={{ marginTop: 3, textAlign: 'center' }}>
                {
                  reporting
                  ? <Button variant='contained' disabled startIcon={<CircularProgress size={20} />}>Wyślij zgłoszenie</Button>
                  : <Button variant='contained' disabled={bladPowodu != null} onClick={report}>Wyślij zgłoszenie</Button>
                }
              </Box>
            </>
          )
          : []
      }
    </ModalBox>
  </Modal>
  )
}