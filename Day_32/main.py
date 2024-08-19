import datetime as dt
import glob
import random
import smtplib as smtp

import pandas as pd
from password import python_mail_password

# Email
my_email = "ultratumba25@gmail.com"

# Files
df = pd.read_csv(r"Day_32\birthdays.csv")
birthday_info = pd.DataFrame.to_dict(df, orient="records")
filename = random.choice(glob.glob(r"Day_32\letter_templates/*.txt"))

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
            connection.login(my_email, password=python_mail_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=info["email"],
                msg=f"Subject:Happy Birthday\n\n{file_content}",
            )
