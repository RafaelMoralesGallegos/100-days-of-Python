import datetime as dt
import os
import random
import smtplib as smtp

from dotenv import load_dotenv

# *Email
load_dotenv()
my_email = os.environ.get("ULTRA_MAIL_MAIL")
password = os.environ.get("ULTRA_MAIL_PASS")
# with smtp.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs=,
#         msg="Subject:Hello\n\nEres Puto",
#     )

# *Datetime
now = dt.datetime.now()
weekday = now.weekday()
# date_of_birth = dt.datetime(year=2000, month=2, day=25)

# *Challenge 1
with open(r"quotes.txt", "r") as data_file:
    quotes = [quote for quote in data_file]

if weekday == 0:
    today_quote = random.choice(quotes)

    with smtp.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Monday Inspiration Quotes\n\n{today_quote}",
        )
