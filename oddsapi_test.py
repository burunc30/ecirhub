import requests
import json

ODDS_API_KEY = "bf9ad2afed0d379aa0fa2f756dc58ff2"

url = "https://api.the-odds-api.com/v4/sports/soccer_epl/odds/"

params = {
    "regions": "eu",
    "markets": "h2h",
    "oddsFormat": "decimal",
    "apiKey": ODDS_API_KEY
}

response = requests.get(url, params=params)

if response.status_code != 200:
    print("API bağlantı xətası:", response.status_code, response.text)
else:
    data = response.json()
    if not data:
        print("❌ Heç bir oyun tapılmadı.")
    else:
        print(f"✅ Tapılan oyun sayı: {len(data)}\n")
        for match in data:
            home_team = match['home_team']
            away_team = match['away_team']
            commence = match['commence_time']
            bookmakers = match['bookmakers']
            print(f"🟢 {home_team} vs {away_team} — {commence}")
            for bookmaker in bookmakers:
                markets = bookmaker['markets']
                for market in markets:
                    if market['key'] == 'h2h':
                        outcomes = market['outcomes']
                        for outcome in outcomes:
                            print(f"  {outcome['name']}: {outcome['price']}")
            print()
