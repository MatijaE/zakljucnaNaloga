# LiveCard - Digitalna Vizitka

📋 Predpogoji

Prepričajte se, da imate na svojem sistemu nameščeno:
- Python 3.8 ali novejši
- pip (Python package manager)

🚀 Navodila za zagon

1. Prenos projekta
# Prenesite ali klonirajte projekt v svojo mapo
cd /pot/do/vašega/projekta

2. Namestitev odvisnosti
# Namestite potrebne Python pakete
pip install flask tinydb tinyrecord bcrypt

Alternativno, če imate `requirements.txt` datoteko:
pip install -r requirements.txt

3. Zagon aplikacije

Razvojni način (za testiranje):
python main.py

Produkcijski način (z Gunicorn):
# Najprej namestite Gunicorn
pip install gunicorn

Zaženite aplikacijo z več delavci
gunicorn -w 4 -b 0.0.0.0:5001 main:app

4. Dostop do aplikacije

Aplikacija bo dostopna na:
- Lokalni dostop: http://localhost:5001
- Mrežni dostop: http://IP_naslov_računalnika:5001

🔑 Privzeti dostopi

Admin dostop:
- Uporabniško ime: `admin`
- Geslo: `admin`

Novo registracija:
- Obiščite `/register` in ustvarite nov račun
- Po registraciji se prijavite z ustvarjenimi podatki

📁 Struktura projekta

LiveCard/
├── main.py                 # Glavna Flask aplikacija
├── users.json             # TinyDB baza uporabnikov (se ustvari samodejno)
├── templates/              # HTML predloge
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── user_dashboard.html
│   ├── profile.html
│   ├── edit_profile.html
│   ├── directory.html
│   ├── public_profile.html
│   └── admin_dashboard.html
├── static/
│   └── style.css          # CSS stili
└── README.md

🌟 Glavne funkcionalnosti

Uporabniške funkcionalnosti:
- ✅ Registracija in prijava uporabnikov
- ✅ Urejanje osebnega profila
- ✅ Dodajanje kontaktnih podatkov in socialnih omrežij
- ✅ Generiranje QR kode za svoj profil
- ✅ Pregled imenika vseh uporabnikov
- ✅ Javni profil dostopen brez prijave

Admin funkcionalnosti:
- ✅ Pregled vseh registriranih uporabnikov
- ✅ Brisanje uporabnikov
- ✅ Ponastavitev gesel uporabnikov

Tehnične funkcionalnosti:
- ✅ Varno hashiranje gesel z bcrypt
- ✅ Upravljanje sej za prijavljene uporabnike
- ✅ Responziven dizajn za mobilne naprave
- ✅ QR koda generiranje z JavaScript knjižnico

🔒 Varnost

- Gesla so varna shranjena z bcrypt hashiranjem
- Admin funkcionalnosti so zaščitene s sejo
- Transakcije z bazo so varne za večuporabniško okolje

🛠️ Razreševanje težav

Aplikacija se ne zažene:
# Preverite Python verzijo
python --version

# Preverite nameščene pakete
pip list

Port 5001 je zaseden:
# Spremenite port v main.py
app.run(host="0.0.0.0", port=5002, debug=True)

Težave z bazo:
# Izbrišite users.json datoteko za popoln reset
rm users.json

📞 Podpora

Za pomoč ali vprašanja se obrnite na:
- Avtor: Matija Eržen
- Email: matija.erzen1@gmail.com
- GitHub: https://github.com/MatijaE/zakljucnaNaloga

---
**LiveCard** - Ustvarite svoj digitalni profil hitro, enostavno, brezplačno! 🚀