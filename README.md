
# 	**ProjektIO** - Projekt zaliczeniowy na na przedmiot: *Inżynieria Oprogramowania*.
## 	Semestr 3 - 2022/23.
##	Autorzy:
  - *Robert Barcik* - [Link do profilu](https://github.com/DidgetPl)
  - *Dominik Breksa* - [Link do profilu](https://github.com/DominikBreksa)
  - *Miłosz Góralczyk* - [Link do profilu](https://github.com/haarmeggido)
  - *Jakub Kot* - [Link do profilu](https://github.com/Eniterusx)
---
## 	Tworzymy *Bota* na platformę *Discord*:
 1. Komendy, na które reaguje:
 	- **!help** - Wyświetla krótki opis wszystkich dostępnych komend.

	- **!upload \<nazwa obrazka> (plik załączony do wiadomości)** – wczytanie oraz wysłanie obrazka do bazy danych membota

	- **!meme** / **!m** – wyświetlenie obrazka z wynikiem większym lub równym 3

	- **!waitingroom** / **!w -** wyświetlenie obrazka z wynikiem mniejszym od 3

	- **!report \<ID obrazka> "\<powód zgłoszenia"** – zgłoszenie treści obrazka do administratorów
	
	- **!see \<ID obrazka>** -  wyświetla obrazek o podanym ID

	Administratorzy mają dodatkowo dostęp do funkcji moderujących:

	- **!ban \<ID zgłoszenia> \<liczba dni> "<powód bana>"** – zbanowanie użytkownika na określoną liczbę dni i usunięcie obrazka z wyświetlanej puli. Taki użytkownik nie może używać komendy !upload

	- **!unban \<ID użytkownika (Discordowe)>** – odbanowanie użytkownika
	
 2. System oceniania:
 	- Nowo dodany obrazek posiada wartość score = 0
 
 	- Użytkownicy mają możliwość oceniania zarówno z posiomu discorda, jak i z poziomu strony

	- Obrazki z oceną score < -4 zostają trwale usuwane

	- Obrazki z oceną > 2 są dostępne pod komendą **!meme / !m**

	- Obrazki z oceną pomiędzy są dostępnepod komendą **!waitingroom / !w**
	
##	*Strona* do dodawania obrazków (wraz z logowaniem, poprzez Discord):
 1. Link do strony *Bota*:
 	[localhost](http://localhost/)
 2. Możliwości strony:
	- **Logowanie się poprzez Discord**
	- **Przeglądanie losowych obrazków**
	- **Ocena obrazków**
	- **Dodawanie nowych obrazków**
	- **Zgłaszanie obrazków**
