# scraper_burunc30.py

import requests
from bot import send_message
from datetime import datetime
import pytz

# Sadə 1xBet API endpoint (təxminidir və stabil deyil — əgər dəyişsə, düzəldərik)
URL = "https://1xbet.com/LineFeed/Get1x2_VZip?sport=1&count=100&lng=en&mode=4&country=1&partner=51"

def get_filtered_matches():
    try:
        response = requests.get(URL, timeout=10)
        data = response.json()
        matches = data.get("Value", [])
        filtered = []

        for match in matches:
            home_team = match.get("O1")
            away_team = match.get("O2")
            start_time = match.get("S")
            odds = match.get("E", [])
            match_time = datetime.utcfromtimestamp(start_time).replace(tzinfo=pytz.utc).astimezone(pytz.timezone('Europe/Baku')).strftime('%Y-%m-%d %H:%M')

            if len(odds) >= 3:
                home_odds = float(odds[0].get("C", 0))
                if home_odds > 2.0:
                    filtered.append(f"{match_time} — {home_team} vs {away_team} | Home odds: {home_odds}")

        return filtered

    except Exception as e:
        return [f"Xəta baş verdi: {e}"]

def main():
    send_message("Burunc30 1xBet sistem başladı (Filter 6Z)")
    matches = get_filtered_matches()
    if matches:
        for m in matches:
            send_message(m)
    else:
        send_message("Filter 6Z üzrə uyğun oyun tapılmadı.")

if __name__ == "__main__":
    main()
