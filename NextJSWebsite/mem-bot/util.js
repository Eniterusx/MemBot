import axios from 'axios'

// Funkcja do requestowania API przez swr
export function fetcher (url) {
  return axios.get(url, { headers: { } }).then((response) => response.data).catch((error) => error.response.data)
}

// no przecież masz nazwę zmiennej poniżej
// (nie no, chodzi o akceptowane przez upload rozszerzenia plików)
export const akceptowaneTypy = {
  'video/mp4': ['.mp4'],
  'image/png': ['.png'],
  'image/gif': ['.gif'],
  'image/jpg': ['.jpg'],
  'image/jpeg': ['.jpeg'],
  'image/apng': ['.apng']
}

// Sophisticated confirmation of the meme images' name
export function czyBladNazwy/*Placówki*/ (nazwa) {
  if (nazwa.length < 2) return "Nazwa powinna składać się z przynajmniej 2 znaków"
  else if (nazwa.length > 70) return "Nazwa powinna składać się z maksymalnie 70 znaków"
  
  const result = /^[\w ąćęłńóśźżł]*$/.exec(nazwa) 
  if (result == null) return "Nazwa może składać się wyłącznie z liter (a-z A-Z), cyfr (0-9), podłogi (_) i spacji ( )."
}

// sprawdź, czy typ pliku jest akceptowany przez serwery AGH
export function czyAkceptowanyTyp (type) {
  return type in akceptowaneTypy  
}

// sprawdź, czy wielkość pliku jest akceptowana przeze mnie (osobiście liczę bajty)
export function czyBladWielkosci (plik) {
  if (plik.readerror) return "Wystąpił błąd podczas wczytywania pliku. Usuń plik i spróbuj ponownie."
  if (plik.data == null) return 'Wczytywanie pliku...'
  // return false // Z gory zaloz ze osiagnieto limit bazy danych
  if (Buffer.byteLength(plik.data.split(',')[1], 'base64') > 25000000) return 'Plik może mieć do 25 mb.'
}

export function czyBladReportu (tekst) {
  if (tekst.length < 5) return "Zgłoszenie powinno składać się z przynajmniej 5 znaków"
  else if (tekst.length > 250) return "Zgłoszenie powinno składać się z maksymalnie 250 znaków"
  const result = /^[\w ąćęłńóśźżł]*$/.exec(tekst) 
  if (result == null) return "Zgłoszenie może składać się wyłącznie z liter (a-z A-Z), cyfr (0-9), podłogi (_) i spacji ( )."
}