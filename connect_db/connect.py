from db import users_db



async def connect_to_user_db(user_id, user_name):
    await users_db.add_new_user(user_id, user_name)
