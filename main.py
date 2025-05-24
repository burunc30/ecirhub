import requests
import time

# API və Telegram məlumatları
ODDS_API_KEY = "bf9ad2afed0d379aa0fa2f756dc58ff2"
TELEGRAM_BOT_TOKEN = "8106341353:AAFIi3nfPOlydtCM_eYHiSIbDR0C1RFoaG4"
CHAT_ID = "1488455191"

def get_odds_data():
    url = "https://api.the-odds-api.com/v4/sports/soccer_epl/odds"
    params = {
        "apiKey": ODDS_API_KEY,
        "regions": "eu",
        "markets": "h2h,draw_no_bet,ht_ft",
        "oddsFormat": "decimal"
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("API error:", response.text)
        return []
    return response.json()

def filter_matches(data):
    filtered = []

    for match in data:
        teams = match.get("teams", [])
        if len(teams) != 2:
            continue
        team_a, team_b = teams[0], teams[1]
        bookmakers = match.get("bookmakers", [])
        if not bookmakers:
            continue

        h2h = draw_no_bet = ht_ft = None
        for b in bookmakers:
            markets = b.get("markets", [])
            for m in markets:
                if m["key"] == "h2h":
                    h2h = m["outcomes"]
                elif m["key"] == "draw_no_bet":
                    draw_no_bet = m["outcomes"]
                elif m["key"] == "ht_ft":
                    ht_ft = m["outcomes"]

        if not h2h:
            continue

        try:
            a_h2h = next(o["price"] for o in h2h if o["name"] == team_a)
            b_h2h = next(o["price"] for o in h2h if o["name"] == team_b)
        except:
            continue

        matched_filters = []

        # Filter 1: Under 2.5 & BTTS Yes – yoxlanacaq halda uyğun market olmadıqda buraxılır
        # Bu API həmin marketləri vermirsə, bu filter aktiv edilməsin

        # Filter 2: 1X2 və HT/FT oddsları ziddiyyətlidir
        if h2h and ht_ft:
            try:
                htft_a = next(o["price"] for o in ht_ft if o["name"] == team_a)
                if b_h2h < a_h2h and htft_a < b_h2h:
                    matched_filters.append("Filter 2")
            except:
                pass

        # Filter 3: Team A 1X2-də favoritdir, amma Draw No Bet-də Team B favoritdir
        if h2h and draw_no_bet:
            try:
                a_dnb = next(o["price"] for o in draw_no_bet if o["name"] == team_a)
                b_dnb = next(o["price"] for o in draw_no_bet if o["name"] == team_b)
                if a_h2h < b_h2h and b_dnb < a_dnb:
                    matched_filters.append("Filter 3")
            except:
                pass

        # Filter 4: 1X2-də Team A favoritdir, amma HT və ya 2nd Half odds-da Team B favoritdir (təxmini model)
        if h2h and ht_ft:
            try:
                htft_b = next(o["price"] for o in ht_ft if o["name"] == team_b)
                if a_h2h < b_h2h and htft_b < a_h2h:
                    matched_filters.append("Filter 4")
            except:
                pass

        if matched_filters:
            match_info = f"{team_a} vs {team_b}\nMatched: {', '.join(matched_filters)}"
            filtered.append(match_info)

    print("Filtrdən keçən matçlar:", filtered)
    return filtered

def send_to_telegram(messages):
    if not messages:
        messages = ["Test: Heç bir uyğun matç tapılmadı."]
    text = "\n\n".join(messages)
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    r = requests.post(url, data=payload)
    print("Telegram status:", r.status_code, r.text)

def main():
    data = get_odds_data()
    filtered = filter_matches(data)
    send_to_telegram(filtered)

if __name__ == "__main__":
    main()
