from aiogram import Bot, Dispatcher
import config

bot = Bot(token=str(config.TOKEN), parse_mode="HTML")
dp = Dispatcher(bot)