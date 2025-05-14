
import time
from bot import send_message
from oddsapi_fetcher import get_oddsapi_matches
from scarping_1xbet import get_1xbet_matches
from filters import apply_filters

if __name__ == "__main__":
    while True:
        try:
            messages = []

            oddsapi_matches = get_oddsapi_matches()
            filtered_oddsapi = apply_filters(oddsapi_matches, "OddsAPI")
            messages.extend(filtered_oddsapi)

            xbet_matches = get_1xbet_matches()
            filtered_xbet = apply_filters(xbet_matches, "1xBet")
            messages.extend(filtered_xbet)

            if messages:
                final_msg = "*Burunc30 - Yeni Filtrlənmiş Oyunlar:*

" + "
".join(messages)
            else:
                final_msg = "Burunc30: Filtrlərə uyğun oyun tapılmadı."

            send_message(final_msg)

        except Exception as e:
            send_message(f"Burunc30-da xəta baş verdi:
{e}")

        time.sleep(1200)
