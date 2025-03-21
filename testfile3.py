# https://www.blog.pythonlibrary.org/2012/07/18/python-a-simple-step-by-step-sqlite-tutorial/
#https://toobamalaika.medium.com/installation-of-sqlite-browser-in-ubuntu-20-04-37e4e78aa51f
import sqlite3 

# Connect to the SQLite database
conn = sqlite3.connect('mydatabase.db')

# Define the query
query = "SELECT MAX(score) FROM movies"
#query = "SELECT COUNT(*) FROM movies WHERE year = 1998;"

# Execute the query and fetch the result
cursor = conn.cursor()
cursor.execute(query)
result = cursor.fetchone()[0]

# Print the result
print(f"Maximum rating in the table: {result}")

# Close the connection
conn.close()
