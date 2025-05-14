import time
import requests

def run_bot():
    TOKEN = "8106341353:AAFIi3nfPOlydtCM_eYHiSIbDR0C1RFoaG4"  # Yeni Telegram bot tokenin
    CHAT_ID = "1488455191"  # Sənin Telegram chat ID-in

    while True:
        text = "Burunc30 sistemi işləyir!"
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
        try:
            response = requests.post(url, data=payload)
            print(f"Mesaj göndərildi: {response.status_code}")
        except Exception as e:
            print(f"Xəta baş verdi: {e}")
        time.sleep(600)  # 10 dəqiqə gözləyir
