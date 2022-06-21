from aiogram import types, Dispatcher
from connect_db import connect



async def gretting(message: types.Message):
    await message.answer(f"Hello my dear {message.from_user.full_name}\n" 
                        "I want to give you inforamtion about our telegram groups <strong><pre>'infomation'," 
                        "'your rules or others'</pre></strong>", parse_mode="HTML")
    user_id = message.from_user.id
    user_name = message.from_user.full_name

    await connect.connect_to_user_db(user_id, user_name)





def register_message_handler_user(dp: Dispatcher):
    dp.register_message_handler(gretting, commands=['start', 'help'])
