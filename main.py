
import requests
from bot import send_message

print("Burunc30 system started...")

API_KEY = "bf9ad2afed0d379aa0fa2f756dc58ff2"
SPORT = "soccer"
REGION = "eu"
FORMAT = "decimal"
URL = f"https://api.the-odds-api.com/v4/sports/{SPORT}/odds/?apiKey={API_KEY}&regions={REGION}&oddsFormat={FORMAT}&markets=h2h,totals,btts,draw_no_bet,half_time,second_half"

try:
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        messages = []

        for match in data:
            home = match.get("home_team")
            away = match.get("away_team")
            bookmakers = match.get("bookmakers", [])
            if not bookmakers:
                continue

            outcomes = {}
            for bm in bookmakers:
                for market in bm.get("markets", []):
                    outcomes[market["key"]] = market.get("outcomes", [])

            h2h = outcomes.get("h2h", [])
            totals = outcomes.get("totals", [])
            btts = outcomes.get("btts", [])
            dnb = outcomes.get("draw_no_bet", [])
            half_time = outcomes.get("half_time", [])
            second_half = outcomes.get("second_half", [])

            home_odds = next((x["price"] for x in h2h if x["name"] == home), None)
            away_odds = next((x["price"] for x in h2h if x["name"] == away), None)

            # Filter 1: Under 2.5 & BTTS: Yes
            under25 = any(x for x in totals if x.get("point") == 2.5 and x["name"] == "Under" and x["price"] < 2.0)
            btts_yes = any(x for x in btts if x["name"] == "Yes" and x["price"] < 2.0)
            if under25 and btts_yes:
                messages.append(f"<b>Filter 1:</b> {home} vs {away} — Under 2.5 + BTTS: Yes")

            # Filter 2: 1X2 vs HT/FT contradiction
            if home_odds and half_time:
                ht_home = next((x["price"] for x in half_time if x["name"] == home), None)
                if ht_home and ht_home > home_odds:
                    messages.append(f"<b>Filter 2:</b> {home} vs {away} — HT favorit dəyişir")

            # Filter 3: 1X2 favorit home, DNB favorit away
            if home_odds and away_odds and home_odds < away_odds:
                dnb_home = next((x["price"] for x in dnb if x["name"] == home), None)
                dnb_away = next((x["price"] for x in dnb if x["name"] == away), None)
                if dnb_home and dnb_away and dnb_away < dnb_home:
                    messages.append(f"<b>Filter 3:</b> {home} vs {away} — 1X2: {home}, DNB: {away}")

            # Filter 4: 1X2 favorit home, Half favorit away
            fh_away = next((x["price"] for x in half_time if x["name"] == away), None)
            sh_away = next((x["price"] for x in second_half if x["name"] == away), None)
            if home_odds and away_odds and home_odds < away_odds:
                if (fh_away and fh_away < away_odds) or (sh_away and sh_away < away_odds):
                    messages.append(f"<b>Filter 4:</b> {home} vs {away} — 1X2: {home}, Half: {away}")

            # Filter 6Z: Home team odds > 2.0
            if home_odds and home_odds > 2.0:
                messages.append(f"<b>Filter 6Z:</b> {home} vs {away} — Home odds: {home_odds}")

        if messages:
            for msg in messages:
                send_message(msg)
        else:
            send_message("Burunc30: Heç bir filtrə uyğun matç tapılmadı.")
    else:
        send_message(f"API xətası: {response.status_code} — {response.text}")
except Exception as e:
    send_message(f"Burunc30 sistemində xəta baş verdi:\n{str(e)}")
