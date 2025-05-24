import requests
import time
API və Telegram məlumatları

ODDS_API_KEY = "bf9ad2afed0d379aa0fa2f756dc58ff2" TELEGRAM_BOT_TOKEN = "8106341353:AAFIi3nfPOlydtCM_eYHiSIbDR0C1RFoaG4" CHAT_ID = "1488455191"

İstifadə olunan bukmeykerlər və bazarlar

BOOKMAKERS = "bet365,williamhill,1xbet" REGIONS = "eu" MARKETS = ["h2h", "draw_no_bet", "halftime", "totals", "both_teams_to_score"]

Telegrama mesaj göndər

def send_telegram_message(message): url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage" payload = { "chat_id": CHAT_ID, "text": message, "parse_mode": "HTML" } requests.post(url, data=payload)

Filter funksiyaları

def filter_matches(events): results = [] for event in events: try: teams = event["teams"] bookmakers = event.get("bookmakers", []) if not bookmakers: continue

odds_data = {}
        for book in bookmakers:
            for market in book.get("markets", []):
                odds_data[market["key"]] = market

        # Filter 1: Under 2.5 + BTTS: Yes
        under_2_5 = False
        btts_yes = False
        if "totals" in odds_data:
            for outcome in odds_data["totals"]["outcomes"]:
                if outcome["point"] == 2.5 and outcome["name"] == "Under" and float(outcome["price"]) >= 1.5:
                    under_2_5 = True
        if "both_teams_to_score" in odds_data:
            for outcome in odds_data["both_teams_to_score"]["outcomes"]:
                if outcome["name"] == "Yes" and float(outcome["price"]) >= 1.5:
                    btts_yes = True

        if under_2_5 and btts_yes:
            results.append((teams, "Filter 1"))
            continue

        # Filter 2: 1X2 vs HT/FT ziddiyyət
        if "h2h" in odds_data and "halftime" in odds_data:
            h2h = odds_data["h2h"]["outcomes"]
            halftime = odds_data["halftime"]["outcomes"]
            h2h_fav = max(h2h, key=lambda x: float(x["price"]))
            half_fav = max(halftime, key=lambda x: float(x["price"]))
            if h2h_fav["name"] != half_fav["name"]:
                results.append((teams, "Filter 2"))
                continue

        # Filter 3: 1X2 favorit A, DNB favorit B
        if "h2h" in odds_data and "draw_no_bet" in odds_data:
            h2h = odds_data["h2h"]["outcomes"]
            dnb = odds_data["draw_no_bet"]["outcomes"]
            h2h_fav = max(h2h, key=lambda x: float(x["price"]))
            dnb_fav = max(dnb, key=lambda x: float(x["price"]))
            if h2h_fav["name"] != dnb_fav["name"]:
                results.append((teams, "Filter 3"))
                continue

        # Filter 4: 1X2 favorit A, HT və ya SH favorit B
        if "h2h" in odds_data and "halftime" in odds_data:
            h2h = odds_data["h2h"]["outcomes"]
            halftime = odds_data["halftime"]["outcomes"]
            h2h_fav = max(h2h, key=lambda x: float(x["price"]))
            half_fav = max(halftime, key=lambda x: float(x["price"]))
            if h2h_fav["name"] != half_fav["name"]:
                results.append((teams, "Filter 4"))
                continue

    except Exception as e:
        print(f"Xəta: {e}")
return results

Əsas funksiyanı işə sal

def main(): url = "https://api.the-odds-api.com/v4/sports/soccer_epl/odds" params = { "apiKey": ODDS_API_KEY, "regions": REGIONS, "markets": ",".join(MARKETS), "bookmakers": BOOKMAKERS } response = requests.get(url, params=params) if response.status_code != 200: send_telegram_message("Odds API bağlantısında problem var.") return

events = response.json()
matched = filter_matches(events)

if matched:
    for teams, reason in matched:
        message = f"<b>{teams[0]} vs {teams[1]}</b>\nUyğun gəldi: {reason}"
        send_telegram_message(message)
else:
    send_telegram_message("Heç bir uyğun matç tapılmadı.")

if name == "main": main()

