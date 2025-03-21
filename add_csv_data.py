import sqlite3
import csv
import pandas as pd

# Connect to database
database = "mydatabase.db"
conn = sqlite3.connect(database) 
cur = conn.cursor()

# Create Table
cur.execute("DROP TABLE IF EXISTS movies;")
cur.execute("CREATE TABLE movies (id, title, score);") # use your column names here

# Add in data from csv file
col_names = ['id', 'title', 'score']
df = pd.read_csv('data/movies.csv', names=col_names, header=None)
df.to_sql('movies', conn, if_exists='append', index=False)

# Commit and close
conn.commit()
conn.close()