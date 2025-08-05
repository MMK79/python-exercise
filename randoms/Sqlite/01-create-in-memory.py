import sqlite3

try:
    with sqlite3.connect(':memory:') as conn:
        print(f"sqlite got created on memory with version {sqlite3.sqlite_version}")
except sqlite3.OperationalError as e:
    print(f"Something went wrong with database {e}")

