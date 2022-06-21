from aiogram.utils import executor
from users import gretting
from db import users_db
from loader import dp


def on_startup(_):
    users_db.strart()



gretting.register_message_handler_user(dp)


if __name__ == "__main__":
    executor.start_polling(on_startup, dispatcher=dp, skip_updates=True)
