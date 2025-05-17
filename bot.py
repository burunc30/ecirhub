import requests
from filters import apply_all_filters
from odds_api import get_odds_api_matches
from x1xbet import get_1xbet_matches

TOKEN = '8106341353:AAFIi3nfPOlydtCM_eYHiSIbDR0C1RFoaG4'
CHAT_ID = '1488455191'

def send_message(text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': text}
    requests.post(url, data=data)

def send_filtered_matches():
    odds_matches = get_odds_api_matches()
    xbet_matches = get_1xbet_matches()
    all_matches = odds_matches + xbet_matches

    results = apply_all_filters(all_matches)
    for match in results:
        send_message(match)