import os

import requests
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.environ.get("NUTRITION_APP_ID")
API_KEY = os.environ.get("NUTRITION_API_KEY")
WEIGHT = 80
HEIGHT = 182.21
AGE = 24

headers = {"x-app-id": APP_ID, "x-app-key": API_KEY}
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")

exercise_param = {
    "query": exercise_text,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=exercise_param, headers=headers)
result = response.json()
