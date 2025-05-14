import time
from bot import send_message

def get_1xbet_matches():
    # Bu, hələlik test üçün sadə saxta datadır.
    return [
        {"home": "Chelsea", "away": "Arsenal", "odds": {"1": 2.10, "X": 3.20, "2": 3.40}, "dnb": {"1": 1.80, "2": 1.90}, "btts": "Yes", "under2_5": "Yes", "htft": {"1/1": 3.5, "2/2": 4.2, "1/2": 28.0}},
        {"home": "Real Madrid", "away": "Barcelona", "odds": {"1": 1.85, "X": 3.40, "2": 4.0}, "dnb": {"1": 1.40, "2": 2.60}, "btts": "Yes", "under2_5": "No", "htft": {"1/1": 2.5, "2/2": 5.5, "1/2": 19.0}},
    ]

def apply_filters(matches):
    result = []

    for m in matches:
        filters_passed = []

        # Filter 1: Under 2.5 + BTTS both Yes
        if m.get("under2_5") == "Yes" and m.get("btts") == "Yes":
            filters_passed.append("Filter 1")

        # Filter 2: Contradiction 1X2 vs HT/FT (e.g. 1 favorite but HT/FT has 1/2 high odds)
        if m["odds"]["1"] < m["odds"]["2"] and m["htft"].get("1/2", 0) > 20:
            filters_passed.append("Filter 2")

        # Filter 3: 1X2 -> team A favorite, but DNB -> team B favorite
        if m["odds"]["1"] < m["odds"]["2"] and m["dnb"]["2"] < m["dnb"]["1"]:
            filters_passed.append("Filter 3")

        # Filter 4: Team A favorite in 1X2 but Team B favorite in HT or 2H odds
        if m["odds"]["1"] < m["odds"]["2"] and m["htft"].get("2/2", 0) < m["htft"].get("1/1", 100):
            filters_passed.append("Filter 4")

        # Filter 5 (6Z): Home team odds > 2.0 in 1X2
        if m["odds"]["1"] > 2.0:
            filters_passed.append("Filter 5")

        if filters_passed:
            result.append(f"*{m['home']} vs {m['away']}*\nPassed: {', '.join(filters_passed)}\nHome odds: {m['odds']['1']}\n")

    return result

if __name__ == "__main__":
    while True:
        try:
            matches = get_1xbet_matches()
            filtered = apply_filters(matches)

            if filtered:
                final_msg = "*Burunc30 - Yeni Filtrlənmiş Oyunlar:*\n\n" + "\n".join(filtered)
            else:
                final_msg = "Burunc30: Filtrlərə uyğun oyun tapılmadı."

            send_message(final_msg)

        except Exception as e:
            send_message(f"Burunc30-da xəta baş verdi:\n{e}")

        time.sleep(1200)  # 20 dəqiqə
