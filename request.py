# 0 = krediver, 1 = verme
# 0 = evsahibi, 1 = kiracı
# 0 = telefon yok, 1 = var
# naive bayes. 7 siniflandirma algoritmasi kullandik. naive bayes 0.712 değeri verdi bu en yüksek.
# feature selection kullanmadık. label encoder kullandık. kayıp veri yoktu.

import requests

# URL
url = 'http://localhost:5000/api/'

# Change the value of experience that you want to test
payload = {
    'krediMiktari': 30,
    "yas": 20,
    "evDurumu": 0,
    "aldigi_kredi_sayi": 2,
    "telefonDurumu": 0
}

r = requests.post(url, json=payload)

if r.json()==1 :
    print("Kredi verilemez")
elif r.json()==0 :
    print("Kredi verilebilir")


