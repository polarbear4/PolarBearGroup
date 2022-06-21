from aiogram.utils import executor
from users import gretting
from db import users_db
import loader


def on_startup(_):
    users_db.strart()



gretting.register_message_handler_user(loader.dp)


if __name__ == "__main__":
    executor.start_polling(loader.dp, on_startup=on_startup, skip_updates=True)
