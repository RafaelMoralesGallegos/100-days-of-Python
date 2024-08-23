import datetime as dt
import os

import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ.get("PIXELA_TOKEN")
USERNAME = "ultratumba"
READ_ID = "ultrareading123"

pixela_endp = "https://pixe.la/v1/users"
graph_endp = f"{pixela_endp}/{USERNAME}/graphs"
pixel_endp = f"{graph_endp}/{READ_ID}"

user_param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_param = {
    "id": READ_ID,
    "name": "My Reading Habbit",
    "unit": "page",
    "type": "int",
    "color": "ajisai",
    "timezone": "America/Mexico_City",
}

today = str(dt.date.today()).replace("-", "")
pixel_add_param = {"date": today, "quantity": "5"}

date_chage = "20240822"
pixel_update_endp = f"{graph_endp}/{READ_ID}/{date_chage}"
pixel_update_param = {"quantity": "8"}

headers = {"X-USER-TOKEN": TOKEN}

# response = requests.post(
#     url=pixel_update_endp, json=pixel_update_param, headers=headers
# )
# response = requests.put(url=pixel_update_endp, json=pixel_update_param, headers=headers)
response = requests.delete(url=pixel_update_endp, headers=headers)
print(response.text)
