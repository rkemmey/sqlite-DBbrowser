import sqlite3
from sqlite3 import Error
import csv

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
    except Error as e:
        print("Error occurred: " + str(e))

    return connection

def execute_query(connection, query):
    cursor = connection.cursor() #create cursor on connection instance to execute queries
    try:
        if query == "":
            return "Query Blank"
        else:
            cursor.execute(query)
            connection.commit()
            return "Query executed successfully"
    except Error as e:
        return "Error occurred: " + str(e)

def main():
    database = "mydatabase.db" # creates db file
    try:
        conn = create_connection(database)
        if conn is not None:
            print(f"Connection to {database} successful!")
            #conn.close() 
    except:
        print("Database Creation Error")

if __name__ == '__main__':
    main()

#sudo apt-get install sqlitebrowser