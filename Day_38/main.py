import os

from dotenv import load_dotenv

load_dotenv()

APP_ID = os.environ.get("NUTRITION_APP_ID")
API_KEY = os.environ.get("NUTRITION_API_KEY")
