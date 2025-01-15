import os
import smtplib as smtp
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()

MY_LAT = 20.620343
MY_LNG = -103.444140
MY_POSITION = (MY_LAT, MY_LNG)
MY_EMAIL = os.environ.get("ULTRA_MAIL_MAIL")
MY_PASSWORD = os.environ.get("ULTRA_MAIL_PASS")


def in_position(my_position) -> bool:
    try:
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching ISS data: {e}")
        return False
    else:
        data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_position = (iss_latitude, iss_longitude)

    return (my_position[0] - 5 <= iss_position[0] <= my_position[0] + 5) and (
        my_position[1] - 5 <= iss_position[1] <= my_position[1] + 5
    )


def is_dark() -> bool:
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
        "tzid": "America/Mexico_City",
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    return sunrise > time_now or time_now > sunset


# -------10--------20--------30--------40--------50--------60--------70#
if in_position(MY_POSITION) and is_dark():
    with smtp.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=(
                f"Subject:Look Up\n\nLook Up Stupid!!"
                f"\nISS is here don't be shuch a falire"
            ),
        )
