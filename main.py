import requests
import pandas as pd
import os
import psycopg2



from sqlalchemy import create_engine
from managers import df_managers
from matches import df_completed_matches
from dotenv import load_dotenv

# Use the existing SQLTools connection
connection_string = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
engine = create_engine(connection_string)

# Load the Managers DataFrame into the PostgreSQL table
#df_managers.to_sql('Managers', engine, if_exists='replace', index=False)

#Load the Matches dataframe into the PostgreSQL table
df_completed_matches.to_sql('Matches', engine, if_exists='replace', index=False)

print("DataFrame loaded to PostgreSQL table successfully.")