from email.mime import base
import psycopg2 as sq
import config

base = sq.connect(config.URI)
cursor = base.cursor()

def strart():
    cursor.execute("CREATE TABLE IF NOT EXISTS users(id INT, user_name TEXT)")
    

async def add_new_user(user_id, user_name):
    check = cursor.execute(f"SELECT id FROM users WHERE id={user_id}").fetchone()
    if check is None:
        cursor.execute("INSERT INTO users VALUES(?,?)", (user_id, user_name,))
        base.commit()
    else:
        return
