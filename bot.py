import requests

def send_message(text):
    TOKEN = "8106341353:AAFIi3nfPOlydtCM_eYHiSIbDR0C1RFoaG4"
    CHAT_ID = "1488455191"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    requests.post(url, data=payload)
