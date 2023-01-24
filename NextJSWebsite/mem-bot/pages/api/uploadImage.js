import conPromise from '../../database'
import axios from 'axios'

import { czyBladNazwy, czyAkceptowanyTyp, czyBladWielkosci } from '../../util.js'
import imgurConfig from '../../imgur.js'
import getSession from '../../session.js'

export default async function handler(req, res) {
  const session = await getSession(req)
  if (!session) return res.status(403).json({ error: 'Nie jesteś zalogowany.' })

  // Potwierdz ze nazwy plikow sa stonks
  for (const file of req.body) {
    // Nazwa
    if (czyBladNazwy(file.name)) return res.status(400).json({ error: `Plik ${file.name} zawiera niedozwoloną nazwę.` })
    // Typ
    if (!czyAkceptowanyTyp(file.type)) return res.status(400).json({ error: `Plik ${file.name} zawiera niedozwolony typ.` })
    // Wielkosci
    if (czyBladWielkosci(file)) return res.status(400).json({ error: `Plik ${file.name} jest zbyt duży.`})
  }

  // Upload plikow do ufoludków na imgurze
  const uploady = []

  for (const file of req.body) {
    const upload = axios.post('https://api.imgur.com/3/upload', {
      image: file.data.split(',')[1], // Plik w base64
      type: 'base64', // Rodzaj danej (tu: base64)
      name: `[MEMESITE] ${file.name}`, // Nazwa uploadu na imgurze
      description: `${file.name} (${file.id})` // Opis uploadu na imgurze
    }, {
      headers: {
        Authorization: `Bearer ${imgurConfig.accessToken}` // Autoryzacja użytkownika imo
        // Please bear with me as I bring your beer
      }
    }).then((response) => response.data).catch((error) => error.response.data)
    .then((data) => {
      // Zmienia przechowywane informacje w oparciu na odpowiedz
      return {
        status: data.status, // http code odpowiedzi
        success: data.success, // czy odpowiedz pomyslna
        error: data?.data?.error, // blad jesli dostepny
        link: data?.data?.link, // link jesli dostepny
        id: data?.data?.id, // id linku do imgur
        deletehash: data?.data?.deletehash, // hash potrzebny do usuniecia pliku
        data: file // oryginalne dane o pliku
      }
    })
    uploady.push(upload) // Dodajemy promise-a do arrayów uploadów
  }

  // Upload plików do bazy danych
  const resolvedUploady = await Promise.all(uploady) // Czekomy na zrealizowanie wszelkich uplołdów

  // Upload do ~~szajsowej~~ swietnej 250MB bazy danych AGH (nie moglem nawet wrzucic plików w rawie i musiałem użyć własnego konta na imgurze
  // a wy chcecie szkolić ludzi do "Big" data)
  const rekordy = []
  
  for (const file of resolvedUploady) {
    if (file.success) { // Jeżeli zrealizowano upload wysylamy zdjecie do bazy
      const upload = conPromise('INSERT INTO `pictures` (user_id, file_name, file_type, url, image_hash, delete_hash, image_category) VALUES (?, ?, ?, ?, ?, ?, ?);',
        [session.user.user_id, file.data.name, file.data.type, file.link, file.id, file.deletehash, "Empty"])
        .then(() => true) // Zostawiamy wartość true jeżeli się uda
        .catch(() => false) // False jeżeli nie
      rekordy.push(upload) // Wrzucamy promise-a do arrayów uploadów
    }
  }

  const resolvedRekordy = await Promise.all(rekordy) // Czekamy na zrealizowanie wszelkich rekordzistów

  // handling blendow (niestety nie ortograficznych ~~ani językowych~~ ~~kardynalnych też~~ [ale stylistyczne juz tak])
  let /*twoje_zyciowe_*/ bledy = []
  for (const uploadId in resolvedUploady) {
    // Sprawdzamy bledy z uploadów na imgura
    const upload = resolvedUploady[uploadId] // Wartości zwrócone z promise-ów
    if (upload.error) { // Jeżeli jest w nich błąd
      bledy.push(uploadId)
      // ayyyy caramba
      console.log(`Nie udało się uploadować ${upload.data.name} - błąd imgur ${upload.error} [${upload.status}]`)
    }
  }
  for (const rekordId in resolvedRekordy) {
    // Sprawdzamy błędy z rekordów do db
    const rekordy = resolvedRekordy[rekordId]
    if (!rekordy) {
      bledy.push(rekordId)
      // tzn w AGHu znów brakło prądu
      // błąd bazy - czyli cringe
      console.log(`Nie udało się uploadować ${upload.data.name} - błąd bazy`)
    }
  }
  
  // TODO: Automatyczna rejestracja do 1000 newsletterów
  // ^ juz zrobilem, ale nie mowcie nikomu
  
  if (bledy > 0) return res.status(500).json({ error: `Nie udało się dodać ${bledy} zdjęć:${bledy.map((plikId) => `\n${req.body[plikId].name}`)}` })
  return res.status(200).json({}) // "u mnie działa"
}
export const config = {
  api: {
    bodyParser: {
      // Zobacz jak powalił mysqla AGH w 2.5 requestów
      // mogę zapchać całą bazę w 3 requesty? trochę przyps
      // "Nic dwa razy się nie zdarza" ~~ Sarah
      // a to git
      sizeLimit: '100mb' // limit plikow
    }
  }
}