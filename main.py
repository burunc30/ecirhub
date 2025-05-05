from bot import send_message
from leagues import accepted_leagues

def check_matches():
    # Dummy data, replace with real match and odds fetching
    matches = [{"league": "Albania 1. Division", "home_team": "Team A", "away_team": "Team B", "home_odds": 2.10}]
    for match in matches:
        if match["league"] in accepted_leagues and match["home_odds"] > 2.0:
            msg = f"Match: {match['home_team']} vs {match['away_team']}\nLeague: {match['league']}\nHome Odds: {match['home_odds']}"
            send_message(msg)

if __name__ == "__main__":
    check_matches()
