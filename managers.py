from source import df_league_entries


df_managers = df_league_entries.loc[:, ["entry_name", "entry_id", "player_first_name", "player_last_name"]]
df_managers = df_managers.rename(columns={"entry_name": "teamName", "entry_id": "teamId", "player_first_name": "firstName", "player_last_name": "lastName"})
