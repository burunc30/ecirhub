from bot import send_message

print('Burunc30 system starting...')

try:
    send_message("Test mesajı: Burunc30 sistemi Heroku üzərində uğurla işə düşdü!")
    print('Telegram mesajı uğurla göndərildi.')
except Exception as e:
    print(f'Telegram mesajı göndərilə bilmədi. Xəta: {e}')
