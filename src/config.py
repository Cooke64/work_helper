import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
DB_PORT = os.getenv('DB_PORT')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_DATABASE = os.getenv('DB_DATABASE')
DB_HOST = os.getenv('DB_HOST')
DEBUG = (os.getenv('DEBUG') == 'True')

REDIS_HOST = 'localhost' if DEBUG else os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")

ADMINS_ID = []

try:
    ADMINS_ID.extend(list(map(int, os.getenv('ADMINS_ID').split(','))))
except AttributeError:
    pass

local_url = 'postgresql://postgres:12345678@localhost:5432/telegram'
server_url = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'
DATABASE_URI = local_url if DEBUG else server_url
