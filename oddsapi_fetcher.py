
import requests

ODDS_API_KEY = "bf9ad2afed0d379aa0fa2f756dc58ff2"
REGIONS = "eu"
MARKETS = "h2h"
BOOKMAKERS = "bet365"

def get_oddsapi_matches():
    url = f"https://api.the-odds-api.com/v4/sports/soccer_epl/odds/?regions={REGIONS}&markets={MARKETS}&bookmakers={BOOKMAKERS}&apiKey={ODDS_API_KEY}"
    response = requests.get(url)
    data = response.json()

    matches = []
    for event in data:
        home = event['home_team']
        away = event['away_team']
        odds_data = event['bookmakers'][0]['markets'][0]['outcomes']

        odds_dict = {}
        for item in odds_data:
            if item['name'] == home:
                odds_dict["1"] = item['price']
            elif item['name'] == away:
                odds_dict["2"] = item['price']
            elif item['name'] == "Draw":
                odds_dict["X"] = item['price']

        matches.append({
            "home": home,
            "away": away,
            "odds": odds_dict,
            "dnb": {"1": 2.0, "2": 2.0},
            "btts": "Yes",
            "under2_5": "Yes",
            "htft": {"1/1": 3.5, "2/2": 4.2, "1/2": 28.0}
        })

    return matches
