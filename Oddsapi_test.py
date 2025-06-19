import requests
import json

ODDS_API_KEY = "bf9ad2afed0d379aa0fa2f756dc58ff2"  # Sənin OddsAPI açarındır
SPORT = "soccer"  # Futbol üçün
REGION = "eu"     # Avropa bölgəsi (AB, İngiltərə və s.)
MARKET = "h2h"    # 1X2 bazarı

url = f"https://api.the-odds-api.com/v4/sports/{SPORT}/odds"

params = {
    "apiKey": ODDS_API_KEY,
    "regions": REGION,
    "markets": MARKET,
    "oddsFormat": "decimal"
}

response = requests.get(url, params=params)

if response.status_code != 200:
    print(f"❌ Xəta: Status kod {response.status_code}")
    print(response.text)
else:
    data = response.json()
    print(f"✅ Uğurlu! Toplam matç sayı: {len(data)}")
    print("Nümunə matç:")
    if data:
        sample = data[0]
        print(json.dumps(sample, indent=2))
    else:
        print("⚠️ Heç bir matç qaytarılmadı.")
