# app.py

# -- bot.py hissəsi --
import requests

TOKEN = "8106341353:AAFIi3nfPOlydtCM_eYHiSIbDR0C1RFoaG4"
CHAT_ID = "1488455191"
def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    requests.post(url, data=payload)

send_message("Burunc30 sistemi Render üzərində işə başladı!")

# -- main.py hissəsi (filtrlər buraya) --
import time

def run_filters():
    # Buraya filtr kodlarını yerləşdir
    send_message("Filtrlər işlədi və nəticə tapıldı!")  # test mesajı

# Sonsuz dövr – hər 1 saatdan bir filtrləri işlədir
while True:
    run_filters()
    time.sleep(3600)  # 1 saat
