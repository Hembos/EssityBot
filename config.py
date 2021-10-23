from os import environ
from dotenv import load_dotenv

load_dotenv()

TOKEN = environ.get(key="TOKEN")
ADMIN_ID = environ.get(key="ADMIN_ID")
