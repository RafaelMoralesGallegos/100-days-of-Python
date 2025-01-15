import datetime as dt
import glob
import os
import random
import smtplib as smtp

import pandas as pd
from dotenv import load_dotenv

# *Email
load_dotenv()
my_email = os.environ.get("ULTRA_MAIL_MAIL")
password = os.environ.get("ULTRA_MAIL_PASS")

# Files
df = pd.read_csv(r"birthdays.csv")
birthday_info = pd.DataFrame.to_dict(df, orient="records")
filename = random.choice(glob.glob(r"letter_templates/*.txt"))

# Today
today = (dt.datetime.now().month, dt.datetime.now().day)

for info in birthday_info:
    if info["month"] == today[0] and info["day"] == today[1]:
        person_info = info
        with open(filename, "r") as letter:
            file_content = letter.read()
            file_content = file_content.replace("[NAME]", info["name"])

        with smtp.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=info["email"],
                msg=f"Subject:Happy Birthday\n\n{file_content}",
            )
