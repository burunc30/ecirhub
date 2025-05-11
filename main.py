from bot import send_message
from filters import (
    filter_1_btts_under25,
    filter_2_contradiction_1x2_htft,
    filter_3_1x2_vs_dnb,
    filter_4_half_odds_contradiction
)

send_message("Burunc30 sistemi Heroku üzərində işə başladı!")

# Filter 1: BTTS + Under 2.5
matches_1 = filter_1_btts_under25()
for match in matches_1:
    send_message(f"Filter 1: {match['home']} vs {match['away']} | Odds: {match['odds']} | Time: {match['time']}")

# Filter 2: 1X2 vs HT/FT contradiction
matches_2 = filter_2_contradiction_1x2_htft()
for match in matches_2:
    send_message(f"Filter 2: {match['home']} vs {match['away']} | Odds: {match['odds']} | Time: {match['time']}")

# Filter 3: 1X2 vs Draw No Bet
matches_3 = filter_3_1x2_vs_dnb()
for match in matches_3:
    send_message(f"Filter 3: {match['home']} vs {match['away']} | Odds: {match['odds']} | Time: {match['time']}")

# Filter 4: 1X2 vs Half odds contradiction
matches_4 = filter_4_half_odds_contradiction()
for match in matches_4:
    send_message(f"Filter 4: {match['home']} vs {match['away']} | Odds: {match['odds']} | Time: {match['time']}")

print("Burunc30 system finished run.")
