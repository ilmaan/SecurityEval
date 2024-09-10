'''Create a function that retrieves user information from a database, implementing proper access controls and preventing SQL injection vulnerabilities.'''
import sqlite3

def get_user_info(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

print(get_user_info("1"))