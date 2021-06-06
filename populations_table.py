import sqlite3
# create the connection object
conn = sqlite3.connect("new.db")
# get a cursor object used to execute SQL commands
cursor = conn.cursor()
try:
# insert data
    cursor.execute("""CREATE TABLE Populations
        (City TEXT, State TEXT, Population INT)""")
    cursor.execute("INSERT INTO populations VALUES('New York City', 'NY', 8400000)"
    )
    cursor.execute("INSERT INTO populations VALUES('San Francisco', 'CA', 800000)"
    )
# commit the changes
    conn.commit()
except sqlite3.OperationalError:
    print("Oops! Something went wrong. Try again...")
# close the database connection
    conn.close()
