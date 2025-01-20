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

# Transform the data
team1 = df_completed_matches.loc[:, ["gameweek", "finished", "team1", "team1Points", "match_id"]].rename(
    columns={"team1": "team", "team1Points": "points"}
)
team2 = df_completed_matches.loc[:, ["gameweek", "finished", "team2", "team2Points", "match_id"]].rename(
    columns={"team2": "team", "team2Points": "points"}
)

# Combine into a single normalized DataFrame
df_normalized_matches = pd.concat([team1, team2], ignore_index=True)
df_normalized_matches.sort_values(by=["gameweek", "match_id"], inplace=True)

