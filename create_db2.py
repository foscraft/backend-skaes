import sqlite3
from sqlite3 import Error


def create_database():
    """
    Create a new database and 
    -> Pass a name of your choice for the database below.
    DB Will be created on the fly.
    """
    conn = None
    try:
        conn = sqlite3.connect('n_database')
    except Error as e:
        print(e)
    #return conn
    c =conn.cursor()
    c.execute( '''
            CREATE TABLE IF NOT EXISTS users_table
            ([id] INTEGER PRIMARY KEY, 
            [username] VARCHAR NOT NULL, 
            [password] VARCHAR NOT NULL, 
            [email] VARCHAR NOT NULL)
            '''
            )
    conn.commit()

create_database()