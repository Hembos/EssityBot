from os import environ
from dotenv import load_dotenv

load_dotenv()

TOKEN = environ.get(key="TOKEN")
ADMIN_ID = environ.get(key="ADMIN_ID")
DATABASE_URL = environ.get(key="DATABASE_URL")
VIEWERS_EMAILS = environ.get(key="VIEWERS_EMAILS").split(',')
BOT_EMAIL = environ.get(key="BOT_EMAIL")
BOT_EMAIL_PASSWORD = environ.get(key="BOT_EMAIL_PASSWORD")
