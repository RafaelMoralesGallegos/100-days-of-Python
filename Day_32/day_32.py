import datetime as dt
import random
import smtplib as smtp

from password import python_mail_password

# *Email
my_email = "ultratumba25@gmail.com"
password = python_mail_password
# with smtp.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="rafamoralesg25@gmail.com",
#         msg="Subject:Hello\n\nEres Puto",
#     )

# *Datetime
now = dt.datetime.now()
weekday = now.weekday()
# date_of_birth = dt.datetime(year=2000, month=2, day=25)

# *Challenge 1
with open(r"Day_32\quotes.txt", "r") as data_file:
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
