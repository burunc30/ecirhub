def filter_1x2_and_btts(match):
    return match.get("1x2") and match.get("btts") == "Yes"

def filter_odds_conflict(match):
    return match.get("1x2") and match.get("ht_ft") and match["1x2"] != match["ht_ft"]

def filter_draw_no_bet_conflict(match):
    return match.get("1x2") and match.get("dnb") and match["1x2"]["fav"] != match["dnb"]["fav"]

def filter_half_conflict(match):
    return match.get("1x2") and (match.get("first_half") or match.get("second_half"))

def apply_all_filters(matches):
    results = []
    for m in matches:
        if (filter_1x2_and_btts(m) or filter_odds_conflict(m) or
            filter_draw_no_bet_conflict(m) or filter_half_conflict(m)):
            results.append(m)
    return results
