
import requests

def send_message(text):
    TOKEN = "8106341353:AAFVdOReCiCnhdqHq-F0z3rjf-89YrHso8E"
    CHAT_ID = "1488455191"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"}
    requests.post(url, data=payload)
