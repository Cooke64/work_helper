import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

DATABASE_URI = 'postgresql://postgres:12345678@localhost:5432/telegram'

TOKEN = '5643549852:AAF7FnnXnUk7xGQmshGZMbJ4xp89sNZDygY'

ADMINS_ID = [
    514541144,
]
DB_PORT = str(os.getenv('DB_PORT'))
DB_USERNAME = str(os.getenv('DB_USERNAME'))
DB_PASSWORD = str(os.getenv('DB_PASSWORD'))
DB_DATABASE = str(os.getenv('DB_DATABASE'))
DB_HOST = str(os.getenv('DB_HOST'))

f = (
    f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}")

