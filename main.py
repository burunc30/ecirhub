from bot import send_message
from odds_api import (
    filter_1_btts_under25,
    filter_2_contradiction_1x2_htft,
    filter_3_1x2_vs_dnb,
    filter_4_half_odds_contradiction,
    filter_6z_home_odds_gt_2
)

send_message("Burunc30 sistemi Heroku üzərində yenilənmiş filtrlərlə işə düşdü!")

filters = {
    "Filter 1 (BTTS + Under 2.5)": filter_1_btts_under25,
    "Filter 2 (1X2 vs HT/FT)": filter_2_contradiction_1x2_htft,
    "Filter 3 (1X2 vs DNB)": filter_3_1x2_vs_dnb,
    "Filter 4 (1X2 vs Half Odds)": filter_4_half_odds_contradiction,
    "Filter 6Z (Home odds > 2.0)": filter_6z_home_odds_gt_2
}

for name, func in filters.items():
    try:
        matches = func()
        if matches:
            for m in matches:
                msg = f"**{name}**\n⚽ {m['home']} vs {m['away']}\nVaxt: {m['time']}\nƏmsallar: {m['odds']}"
                send_message(msg)
        else:
            send_message(f"{name} üçün uyğun oyun tapılmadı.")
    except Exception as e:
        send_message(f"{name} üçün xəta: {e}")
