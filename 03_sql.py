import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    cities = [
        ('Boston', 'MA', 60000),
        ('Chicago', 'LA', 270000),
        ('Houston', 'TX', 210000),
        ('Phoneix', 'AZ', 150000)
        ]

    c.executemany('INSERT INTO population VALUES(?,?,?)', cities)
    
