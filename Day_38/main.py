import datetime as dt
import os

import requests
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.environ.get("NUTRITION_APP_ID")
API_KEY = os.environ.get("NUTRITION_API_KEY")
AUTHORIZE = os.environ.get("WORKOUT_SHEETY_AUTH")
SHEET_ENDPOINT = os.environ.get("WORKOUT_SHEETY_ENDPOINT")
WEIGHT = 80
HEIGHT = 182.21
AGE = 24

date_today = dt.datetime.now().strftime("%d/%m/%Y")
time_now = dt.datetime.now().strftime("%X")

exercise_headers = {"x-app-id": APP_ID, "x-app-key": API_KEY}
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")

exercise_param = {
    "query": exercise_text,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(
    url=exercise_endpoint,
    json=exercise_param,
    headers=exercise_headers,
)
result = response.json()

for workout in result["exercises"]:
    sheet_param = {
        "workout": {
            "date": date_today,
            "time": time_now,
            "exercise": workout["name"].title(),
            "duration": workout["duration_min"],
            "calories": workout["nf_calories"],
        }
    }
    sheet_headers = {"Authorization": AUTHORIZE}
    sheet_response = requests.post(
        url=SHEET_ENDPOINT, headers=sheet_headers, json=sheet_param
    )
