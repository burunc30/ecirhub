from odds_api import get_odds_api_matches
from x1bet_scraper import get_1xbet_matches
from filters import apply_all_filters
from telegram_bot import send_matches_to_telegram

def main():
    odds_api_matches = get_odds_api_matches()
    x1bet_matches = get_1xbet_matches()

    all_matches = odds_api_matches + x1bet_matches
    filtered_matches = apply_all_filters(all_matches)

    if filtered_matches:
        send_matches_to_telegram(filtered_matches)
    else:
        send_matches_to_telegram(["Uyğun matç tapılmadı."])

if __name__ == "__main__":
    main()
