from aiogram.utils import executor
from users import gretting
from db import users_db
import loader


def on_startup(_):
    users_db.strart()



gretting.register_message_handler_user(loader.dp)


if __name__ == "__main__":
<<<<<<< HEAD
    executor.start_polling(loader.dp, on_startup=on_startup, skip_updates=True)
=======
    executor.start_polling(loader.dp, skip_updates=True, on_start)
>>>>>>> 060cd5dd6baed22f74846c09b3098294b9624a7d
