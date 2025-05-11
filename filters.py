import requests
from datetime import datetime

API_KEY = "bf9ad2afed0d379aa0fa2f756dc58ff2"
BASE_URL = "https://api.the-odds-api.com/v4/sports/soccer/odds"

def get_odds_data(markets):
    params = {
        "apiKey": API_KEY,
        "regions": "eu",
        "markets": markets,
        "oddsFormat": "decimal"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"API xətası: {response.status_code} — {response.text}")
        return []

def filter_1_btts_under25():
    matches = get_odds_data("btts,totals")
    result = []
    for match in matches:
        btts = next((o for o in match['bookmakers'][0]['markets'] if o['key'] == 'btts'), None)
        totals = next((o for o in match['bookmakers'][0]['markets'] if o['key'] == 'totals'), None)
        if btts and totals:
            btts_yes = next((out for out in btts['outcomes'] if out['name'] == 'Yes'), None)
            under_25 = next((out for out in totals['outcomes'] if out['name'] == 'Under 2.5'), None)
            if btts_yes and under_25:
                result.append({
                    "home": match['home_team'],
                    "away": match['away_team'],
                    "odds": f"BTTS: {btts_yes['price']}, Under 2.5: {under_25['price']}",
                    "time": match['commence_time']
                })
    return result

def filter_2_contradiction_1x2_htft():
    matches = get_odds_data("h2h,ht_ft")
    result = []
    for match in matches:
        h2h = next((m for m in match['bookmakers'][0]['markets'] if m['key'] == 'h2h'), None)
        htft = next((m for m in match['bookmakers'][0]['markets'] if m['key'] == 'ht_ft'), None)
        if h2h and htft:
            fav_team = max(h2h['outcomes'], key=lambda x: x['price'])
            contradiction = any(fav_team['name'] not in o['name'] for o in htft['outcomes'])
            if contradiction:
                result.append({
                    "home": match['home_team'],
                    "away": match['away_team'],
                    "odds": f"H2H fav: {fav_team['name']} ({fav_team['price']})",
                    "time": match['commence_time']
                })
    return result

def filter_3_1x2_vs_dnb():
    matches = get_odds_data("h2h,draw_no_bet")
    result = []
    for match in matches:
        h2h = next((m for m in match['bookmakers'][0]['markets'] if m['key'] == 'h2h'), None)
        dnb = next((m for m in match['bookmakers'][0]['markets'] if m['key'] == 'draw_no_bet'), None)
        if h2h and dnb:
            h2h_fav = max(h2h['outcomes'], key=lambda x: x['price'])
            dnb_fav = max(dnb['outcomes'], key=lambda x: x['price'])
            if h2h_fav['name'] != dnb_fav['name']:
                result.append({
                    "home": match['home_team'],
                    "away": match['away_team'],
                    "odds": f"1X2: {h2h_fav['name']} ({h2h_fav['price']}), DNB: {dnb_fav['name']} ({dnb_fav['price']})",
                    "time": match['commence_time']
                })
    return result

def filter_4_half_odds_contradiction():
    matches = get_odds_data("h2h,first_half")
    result = []
    for match in matches:
        h2h = next((m for m in match['bookmakers'][0]['markets'] if m['key'] == 'h2h'), None)
        first_half = next((m for m in match['bookmakers'][0]['markets'] if m['key'] == 'first_half'), None)
        if h2h and first_half:
            h2h_fav = max(h2h['outcomes'], key=lambda x: x['price'])
            fh_fav = max(first_half['outcomes'], key=lambda x: x['price'])
            if h2h_fav['name'] != fh_fav['name']:
                result.append({
                    "home": match['home_team'],
                    "away": match['away_team'],
                    "odds": f"1X2: {h2h_fav['name']} ({h2h_fav['price']}), 1H: {fh_fav['name']} ({fh_fav['price']})",
                    "time": match['commence_time']
                })
    return result
