# LiveCard - digitalna vizitka

## 1. **App funkcije**

- **Shranjevanje vseh kontaktnih podatkov**  
  Vse kontaktne informacije uporabnika, vključno s telefonskimi številkami, e-poštami, socialnimi omrežji, bodo shranjene v digitalnem profilu.

- **Unikatna povezava za vsak profil**  
  Vsak uporabnik bo imel svojo edinstveno povezavo do profila, ki ga bo lahko delil z drugimi.

- **Deljenje podatkov preko QR kode**  
  Uporabniki bodo lahko hitro delili svoje podatke s preprostim skeniranjem QR kode.

- **Možnost dodajanja profilnih slik**  
  Uporabniki bodo lahko dodali svojo profilno sliko, ki bo osebno prilagodila njihov digitalni vizitki.

- **Nastavitev zasebnosti - kaj je lahko dostopno vsem**  
  Uporabniki bodo imeli možnost nastaviti, katere informacije so dostopne javnosti, na primer kontaktne informacije, družbena omrežja, itd.

- **Generiranje vizitke z AI**  
  Aplikacija bo uporabniku omogočila generiranje vizitke z uporabo umetniške inteligence, ki bo lepo razporedila vse podatke.

## 2. **Uporaba markdown**

Markdown je uporabljeno za preprost in pregleden prikaz vseh informacij, brez prekompleksnih oblikovanj. Sledi osnovnim smernicam za ustvarjanje strukturiranega besedila.

## 3. **Izgled - primeri profilov**

Za telefon:
https://github.com/MatijaE/zakljucnaNaloga/blob/main/poslovniDel/telefon_liveCard.png

Za računalnik:
https://github.com/MatijaE/zakljucnaNaloga/blob/main/poslovniDel/rac%CC%8C_liveCard.png

---

## **POSLOVNI DEL (30%)**

### 1. **Identifikacija problema in opis rešitve (5 točk)**

- **Problem:** V današnjem digitalnem svetu so profesionalni in osebni stiki pogosto razdrobljeni po različnih kanalih, kot so e-pošta, telefonske številke, socialna omrežja itd.
              Ni enostavnega načina, kako vse te informacije strniti in jih deliti na hitro in profesionalno.
  
- **Rešitev:** LiveCard omogoča uporabnikom ustvarjanje enotnega digitalnega vizitkastega profila, ki vključuje vse ključne kontaktne podatke.
              Uporabnik lahko profil enostavno deli prek QR kode, kar omogoča enostavno povezovanje v različnih profesionalnih in osebnih nastavitvah.

- **Ciljna skupina:** Profesionalci, podjetniki, mreženje, dogodki in posamezniki, ki želijo hitro in enostavno deliti svoje kontaktne informacije.

### 2. **Analiza trga (5 točk)**

- **Velikost trga:** Trg poslovnega in osebnega omrežja je zelo velik, saj vključuje podjetnike, frizerje, svetovalce, študente in vse, ki redno sodelujejo v mrežnih dogodkih.

- **Konkurenčna analiza:**
  - **Vizitke:** Tradicionalni papirnati vizitki in digitalne alternative kot so LinkedIn.
  - **Prednosti LiveCard:** Hitro in enostavno deljenje vseh podatkov v eni povezavi, vizualno privlačen in prilagodljiv profil, omogočanje deljenja preko QR kode.
  - **Slabosti konkurentov:** Pomanjkanje hitro dostopnih funkcionalnosti za hitro deljenje vseh podatkov v eni enoti.

### 3. **SWOT analiza (5 točk)**

**PREDNOSTI (S)**  
- Enostavna ustvaritev digitalnega profila  
- QR koda za hitro deljenje  
- Prilagodljivost in uporabniška prijaznost

**SLABOSTI (W)**  
- Potrebna kritična masa uporabnikov  
- Potreba po trženju in povečanju zavedanja  
- Zasnova in razvoj dodatnih funkcionalnosti

**PRILOŽNOSTI (O)**  
- Naraščajoča priljubljenost digitalnih vizitk  
- Možnost širjenja na nove trge

**GROŽNJE (T)**  
- Konkurenca večjih platform (npr. LinkedIn)  
- Prepreke pri zaščiti zasebnosti uporabnikov

### 4. **Poslovni model in finančni plan (5 točk)**

- **Viri prihodkov:**
  - Osnovna aplikacija je brezplačna, z možnostjo nadgradnje na premium paket za dostop do naprednih funkcionalnosti (oblikovanje vizitk, dodatne možnosti deljenja).
  - Lahko vključuje tudi partnerske promocije (ponudbe za podjetja).

- **Struktura stroškov:**
  - Razvoj in gostovanje: začetni stroški razvoja in mesečni stroški vzdrževanja.

- **Strategija pridobivanja uporabnikov:**
  - Sodelovanje z organizatorji mrežnih dogodkov, promocije prek socialnih omrežij in influencerjev.

### 5. **Pitch predstavitev (10 točk)**

Predstavitev bo vključevala prikaz prednosti LiveCard aplikacije, demonstracijo delovanja aplikacije z uporabo QR kode ter kako aplikacija rešuje problem in povezuje uporabnike na enostaven način.

---

## **TEHNIČNI DEL (70%)**

### 1. **Flask osnove (15 točk)**

- **Struktura projekta:** Flask aplikacija, ki sledi dobro organiziranim mapam za model, uporabniški sistem in vmesnike.
- **Zagon z gunicorn:** Uporaba Gunicorn za produkcijski zagon aplikacije.
- **Routing:** Osnovni routing za aplikacijo (npr. prijava, registracija, profil uporabnika, generiranje QR kode).
- **Templates:** Uporaba Jinja templating za dinamično generiranje HTML strani (npr. profilna stran uporabnika).
- **Rokovanje z napakami:** Obvladovanje napak in prikaz uporabniku prijaznih sporočil.

### 2. **Uporabniški sistem (20 točk)**

- **Registracija in login:** Uporabnik mora imeti možnost registracije, prijave in odjave. Gesla se varno shranijo (uporaba bcrypt ali podobnih metod).
- **Validacija:** Preverjanje veljavnosti vnosov uporabnikov (npr. telefonska številka, e-poštni naslov).
- **Zaščita strani:** Zaščita osebnih podatkov uporabnika s sejo in ustrezno avtentifikacijo.

### 3. **Interakcija z bazo (25 točk)**

- **Modeli in povezave:** Struktura podatkov v bazi (npr. uporabniški profil, shranjevanje kontaktnih podatkov).
- **Dodajanje, iskanje, filtriranje in urejanje zapisov:** Uporabnik lahko dodaja in ureja svoje kontaktne informacije ter dostopa do svojega profila.
- **Brisanje:** Preprečevanje nenamernih brisanj, označevanje kot izbrisano.

### 4. **API & AJAX (10 točk)**

- **AJAX klici:** Dinamično nalaganje podatkov na uporabniški strani (npr. prikaz vseh uporabnikov, podatkov).
- **API endpointi:** Določeni endpointi za obvladovanje uporabniških profilov in podatkov (REST API).

---

## **Zaključek**

LiveCard bo omogočil enostavno in hitro ustvarjanje profesionalnih digitalnih vizitk, ki jih je mogoče deliti z uporabo QR kode. Uporabniki bodo ustvarili profil z vsemi pomembnimi podatki (kontaktni podatki, socialna omrežja, podjetje) in se lahko hitro povežejo s potencialnimi strankami ali sodelavci na dogodkih.
