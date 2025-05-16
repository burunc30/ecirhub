import requests

TOKEN = "8106341353:AAFIi3nfPOlydtCM_eYHiSIbDR0C1RFoaG4"
CHAT_ID = "1488455191"

def send_matches_to_telegram(matches):
    message = ""
    for match in matches:
        message += f"{match.get('team1')} vs {match.get('team2')}\n"
        message += f"1x2: {match.get('1x2')}\nBTTS: {match.get('btts')}\n"
        message += f"O/U: {match.get('over_under')}\nHT/FT: {match.get('ht_ft')}\n"
        message += f"1st Half: {match.get('first_half')} | 2nd Half: {match.get('second_half')}\n\n"
    if not message:
        message = "Uyğun matç tapılmadı."
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": message})
