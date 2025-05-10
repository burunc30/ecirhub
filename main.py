from bot import send_message
import requests

print("Burunc30 system starting...")

try:
    response = send_message("Test mesajı: Burunc30 sistemi Heroku üzərində uğurla işə düşdü!")
    print("Mesaj göndərildi.")
except requests.exceptions.RequestException as e:
    print(f"Xəta: {e}")

print("Burunc30 system running.")
