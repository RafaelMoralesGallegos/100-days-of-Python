import os

import requests
from dotenv import dotenv_values, load_dotenv

load_dotenv()
TOKEN = os.environ.get("PIXELA_TOKEN")
USERNAME = "ultratumba"

pixela_endp = "https://pixe.la/v1/users"
graph_endp = f"{pixela_endp}/{USERNAME}/graphs"

user_param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_param = {
    "id": "ultrareading123",
    "name": "My Reading Habbit",
    "unit": "page",
    "type": "int",
    "color": "ajisai",
    "timezone": "America/Mexico_City",
}

headers = {"X-USER-TOKEN": TOKEN}

# response = requests.post(url=graph_endp, json=graph_param, headers=headers)
# print(response.text)
