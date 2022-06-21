from email.mime import base
import psycopg2 as sq
import config

base = sq.connect(config.URI)
cursor = base.cursor()

def strart():
    cursor.execute("CREATE TABLE IF NOT EXISTS users(id INT, user_name TEXT)")
    

async def add_new_user(id, user_name):
    cursor.execute("INSERT INTO users VALUES(?,?)", (id, user_name,))
    base.commit()