import sqlite3

# if the file is already exist it will just connect, else it will creat it
# conn = sqlite3.connect("my.db")
# when you done with your database
# conn.close

# Or
# You can let it close connection itself
try:
    with sqlite3.connect("my.db") as conn:
        print(f"Opened sqlite database with {sqlite3.sqlite_version} version successfully!")
except sqlite3.OperationalError as e:
    print('Failed to load the database', e)

