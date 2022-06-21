import dotenv
import os
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv("TOKEN")
ADMIN=os.getenv("ADMIN")
CHAT_ID = os.getenv("CHAT_ID")
URI = os.getenv("URI")
