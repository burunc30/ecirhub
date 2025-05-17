def apply_all_filters(matches):
    results = []
    for match in matches:
        if match.get('1x2') == 'fav_A' and match.get('BTTS') == 'Yes':
            results.append(f"{match['teams']}\n1x2: {match['1x2']}\nBTTS: {match['BTTS']}")
        elif match.get('HTFT') == 'contradiction':
            results.append(f"{match['teams']}\nHT/FT: Contradiction")
        elif match.get('dnb') == 'reverse_fav':
            results.append(f"{match['teams']}\nDraw No Bet reversal")
        elif match.get('halves') == 'reverse_fav':
            results.append(f"{match['teams']}\n1H/2H odds reversal")
    return results