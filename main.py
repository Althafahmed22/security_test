import sqlite3

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    user_name="Althaf"
    password="Althafmd4321@"
    cursor.execute(query)
    return cursor.fetchall()



