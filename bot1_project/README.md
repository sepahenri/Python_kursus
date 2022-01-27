# To-Do's
### Tab 1 - Market Overview
Võiks kuvada üldist informatsiooni turu olukorra kohta

Kuvaks näitajaid:
- BTC Hetke hind, 24h %, Volume(24h), vb lisaks ka väike visuaalne graafik
- Fear&Greed index 

Hirmuindeksi ise uuenev pilt: 
<img src="https://alternative.me/crypto/fear-and-greed-index.png" alt="Latest Crypto Fear & Greed Index" />

### Tab 2 - Trade Management
Koosneks peamiselt input väljadest
- Buy Condition (nt. F&G index <= 25)
- Sell Condition (nt. F&G index >= 90)
- initial capital (nt. 10000 $)
- Base currency (nt. USD, EUR)
- Maximum number of entries (nt. 20 tk)
- Position size (in base currency, nt. 500$)
- Sell only in profit? (extra condition. müü ainult siis kui terve portfoolio on profitis)

### Tab 3 - Portfolio Overview
Esialgu teeme DEMO andmebaasiks samas kaustas paikneva excel tabeli - positions.csv

Kõik eelnevalt 
- Kuvaks kõiki hetkel aktiivseid positioone
- oleks võimalus manuaalselt ka positsioone lisada ning eemaldada (nt. positsiooni id järgi)

### Tab 4 - Historical Price Data
Teine andmebaas, samuti excel tabel samas kaustas: Historical Price Data + Historical Fear&Greed index values.
Ajalooline andme baas hõlmaks endas BTC Daily OHLC hindu (päevaküünalde open, high, low, close hinnad) + F&G indeks iga päeva kohta
- UPDATE nupp (kontrollib kas andmebaasist on datat puudu, kui jah, siis lisab puuduva data)