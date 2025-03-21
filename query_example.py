import sqlite3 

# Connect to the SQLite database
conn = sqlite3.connect('mydatabase.db')

# Define the query
query = "SELECT MAX(score) FROM movies"

# Execute the query and fetch the result
cursor = conn.cursor()
cursor.execute(query)
result = cursor.fetchone()[0]

# Print the result
print(f"Maximum rating in the table: {result}")

# Close the connection
conn.close()
