import os
import smtplib as smtp

import requests
from dotenv import load_dotenv

load_dotenv()
my_email = os.environ.get("ULTRA_MAIL_MAIL")
python_mail_password = os.environ.get("ULTRA_MAIL_PASS")

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
MY_LAT = 20.671955
MY_LNG = -103.416504
parameters = {"lat": MY_LAT, "lon": MY_LNG, "cnt": 5, "appid": api_key}

will_rain = False

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()

for hour_date in data["list"]:
    weather = hour_date["weather"][0]["id"]
    if weather < 700:
        # print("Bring an Umbrella")
        # break
        will_rain = True

if will_rain:
    with smtp.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password=python_mail_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Rain\n\nBring an Umbrella Fool!!",
        )
