import sqlite3

# Check Connection
def check_conn(conn):
    try:
        conn.cursor()
        return True
    except Exception as ex:
        return False

# Check Connection base on file activation
# import os
# import psutil
# path = os.path.abspath('my.db')
#
# def is_open(path):
#     for proc in psutil.process_iter():
#         try:
#             files = proc.open_files()
#             if files:
#                 for _file in files:
#                     if _file.path == path:
#                         return True
#         except psutil.NoSuchProcess as err:
#             print(err)
#     return False

database = 'my.db'
sql_statements = [
    """CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY, 
            name text NOT NULL, 
            begin_date DATE, 
            end_date DATE
        );""",

    """CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY, 
            name TEXT NOT NULL, 
            priority INT, 
            project_id INT NOT NULL, 
            status_id INT NOT NULL, 
            begin_date DATE NOT NULL, 
            end_date DATE NOT NULL, 
            FOREIGN KEY (project_id) REFERENCES projects (id)
        );"""]
try:
    # connect return a Connection Object
    with sqlite3.connect(database) as conn:
        print(type(conn))
        print(check_conn(conn))
        # print(is_open(absolute_path))
        print(f"connected to successfully!")
        cursor = conn.cursor()
        # execute statement
        # cursor.execute(sql_statement)
        for statement in sql_statements:
            cursor.execute(statement)
        # to save changes
        conn.commit()

        print("table created successfully!")

        # import os
        # print(os.path.abspath('my.db'))
        # if os.path.exists('my.db'):
        #     print("Yes")
except sqlite3.OperationalError as e:
    print("something went wrong with your database", e)


