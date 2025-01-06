from source import df_league_entries


df_managers = df_league_entries[["entry_name", "entry_id", "player_first_name", "player_last_name"]]
df_managers.rename(columns={"entry_name": "teamName", "entry_id": "teamId", "player_first_name": "firstName", "player_last_name": "lastName"}, inplace=True)
print(df_managers)