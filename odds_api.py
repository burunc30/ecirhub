import requests

API_KEY = "bf9ad2afed0d379aa0fa2f756dc58ff2"
BASE_URL = "https://api.the-odds-api.com/v4/sports/soccer_epl/odds"

def get_data(markets):
    url = f"{BASE_URL}?regions=eu&markets={markets}&oddsFormat=decimal&apiKey={API_KEY}"
    r = requests.get(url)
    if r.status_code != 200:
        raise Exception(f"API xətası: {r.status_code} — {r.text}")
    return r.json()

def filter_1_btts_under25():
    return _mock_filter("btts", "under_2.5")

def filter_2_contradiction_1x2_htft():
    return _mock_filter("1x2", "htft")

def filter_3_1x2_vs_dnb():
    return _mock_filter("1x2", "draw_no_bet")

def filter_4_half_odds_contradiction():
    return _mock_filter("1x2", "1st_half")

def filter_6z_home_odds_gt_2():
    matches = []
    data = get_data("h2h")
    for match in data:
        home = match["home_team"]
        away = match["away_team"]
        time = match["commence_time"]
        for b in match.get("bookmakers", []):
            for m in b.get("markets", []):
                if m["key"] == "h2h":
                    for outcome in m["outcomes"]:
                        if outcome["name"] == home and outcome["price"] > 2.0:
                            matches.append({
                                "home": home,
                                "away": away,
                                "time": time,
                                "odds": outcome["price"]
                            })
    return matches

def _mock_filter(primary_market, secondary_market):
    return [{
        "home": "Team A",
        "away": "Team B",
        "time": "2025-05-12T18:00:00Z",
        "odds": f"{primary_market} vs {secondary_market}"
    }]
