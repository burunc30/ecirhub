import requests
import time

# API və Telegram məlumatları
ODDS_API_KEY = "bf9ad2afed0d379aa0fa2f756dc58ff2"
TELEGRAM_BOT_TOKEN = "8106341353:AAFIi3nfPOlydtCM_eYHiSIbDR0C1RFoaG4"
CHAT_ID = "1488455191"

def get_odds_data():
    url = "https://api.the-odds-api.com/v4/sports/soccer/odds"
    params = {
        "apiKey": ODDS_API_KEY,
        "regions": "eu",
        "markets": "h2h",
        "oddsFormat": "decimal"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("API xətası:", response.status_code)
        return []

def filter_matches(data):
    filtered = []
    for match in data:
        for bookmaker in match.get("bookmakers", []):
            for market in bookmaker.get("markets", []):
                if market["key"] == "h2h":
                    outcomes = market["outcomes"]
                    if len(outcomes) >= 2:
                        home_team = match["home_team"]
                        away_team = match["away_team"]
                        home_odds = outcomes[0]["price"]
                        if home_odds > 2.0:
                            filtered.append(f"{home_team} vs {away_team} | Home Odds: {home_odds}")
    return filtered

def send_to_telegram(messages):
    if not messages:
        return
    text = "\n".join(messages)
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text
    }
    response = requests.post(url, data=data)
    if response.status_code != 200:
        print("Telegram göndəriş xətası:", response.text)

if __name__ == "__main__":
    matches = get_odds_data()
    filtered = filter_matches(matches)
    send_to_telegram(filtered)
