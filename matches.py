import pandas as pd

from source import df_matches

# Filter the DataFrame to include only the matches that have been completed
df_completed_matches = df_matches.loc[df_matches["finished"] == True].copy()
df_completed_matches.rename(columns={
    "event": "gameweek",
    "league_entry_1": "team1",
    "league_entry_1_points": "team1Points",
    "league_entry_2": "team2",
    "league_entry_2_points": "team2Points"},
                            inplace=True)
df_completed_matches.drop(columns=["winning_method", "winning_league_entry","started"], inplace=True)
df_completed_matches['match_id'] = range(1, len(df_completed_matches) + 1)

print(df_completed_matches)