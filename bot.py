
import requests

BOT_TOKEN = "8106341353:AAFIi3nfPOlydtCM_eYHiSIbDR0C1RFoaG4"
CHAT_ID = "1488455191"

def send_message(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"}
    requests.post(url, data=data)
