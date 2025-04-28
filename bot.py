import os
import requests
import time

TOKEN = "8106341353:AAFVdOReCiCnhdqHq-F0z3rjf-89YrHso8E"
CHAT_ID = "1488455191"

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code != 200:
            print("Failed to send message:", response.text)
    except Exception as e:
        print("Error sending message:", e)

if __name__ == "__main__":
    while True:
        send_message("Salam Elçin! Bot aktivdir.")
        time.sleep(3600)  # Hər saatda bir dəfə mesaj göndər