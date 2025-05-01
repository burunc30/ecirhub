
import os
import requests
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_message(message):
    bot = Bot(token=BOT_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=message)

if __name__ == "__main__":
    try:
        send_message("Burunc30 Bot is running successfully on Heroku!")
    except Exception as e:
        print("Error sending message:", str(e))
