import requests
import pandas as pd

league_id = "185044"  # Replace with your league ID
url = f"https://draft.premierleague.com/api/league/{league_id}/details"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()

    # Parse the JSON data into a DataFrame
    df_matches = data["matches"]
    df_standings = data["standings"]
    df_league_entries = data["league_entries"]
    df_matches = pd.DataFrame(df_matches)
    df_standings = pd.DataFrame(df_standings)
    df_league_entries = pd.DataFrame(df_league_entries)
else:
    print(f"Error: {response.status_code}")

print(df_league_entries.head())