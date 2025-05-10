import requests

def send_message(text):
    TOKEN = "6732279364:AAEl-nvXrhRxOg4k6FOaT_K0AgtOAlEx_3c"
    CHAT_ID = "1488455191"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"}
    response = requests.post(url, data=payload)
    print(f"Telegram cavabı: {response.status_code}, {response.text}")
    return response
