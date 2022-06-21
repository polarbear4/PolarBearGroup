from db import users_db



async def connect_to_user_db(id, user_name):
    await users_db.add_new_user(id, user_name)