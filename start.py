from odds_api import get_odds_api_matches
from x1bet_scraper import get_1xbet_matches
from filters import apply_all_filters
from telegram_bot import send_matches_to_telegram

def main():
    odds_api_matches = get_odds_api_matches()
    x1bet_matches = get_1xbet_matches()
    all_matches = odds_api_matches + x1bet_matches
    filtered = apply_all_filters(all_matches)
    send_matches_to_telegram(filtered)

if __name__ == "__main__":
    main()
