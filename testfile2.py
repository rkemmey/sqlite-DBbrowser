import sqlite3
import csv
import pandas as pd

database = "mydatabase.db"
conn = sqlite3.connect(database) 
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS movies;")
cur.execute("CREATE TABLE movies (id, title, score);") # use your column names here

col_names = ['id', 'title', 'score']
df = pd.read_csv('data/movies.csv', names=col_names, header=None)
df.to_sql('movies', conn, if_exists='append', index=False)

conn.commit()
conn.close()