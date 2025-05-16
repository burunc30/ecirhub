import requests

BOT_TOKEN = "8106341353:AAFIi3nfPOlydtCM_eYHiSIbDR0C1RFoaG4"
CHAT_ID = "1488455191"

def send_matches_to_telegram(matches):
    text = "\n\n".join(matches) if isinstance(matches, list) else str(matches)
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }

    response = requests.post(url, data=payload)
    print("Telegram cavabı:", response.status_code, response.text)
