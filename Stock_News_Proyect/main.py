import datetime as dt
import os
import smtplib as smtp

import requests
from pandas.tseries.offsets import BDay

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

my_email = "ultratumba25@gmail.com"
python_mail_password = os.environ.get("MAIL_PASS")


# Functions
def get_two_days_before():
    """Get the 2 Buissness days before"""
    today = dt.date.today()
    yesterday = today - BDay(1)
    before_y = today - BDay(2)
    yesterday = yesterday.to_pydatetime().date()
    before_y = before_y.to_pydatetime().date()

    return str(yesterday), str(before_y)


def get_diference_stocks(data) -> float:
    """Get difference between 2 buissness days"""
    times_series_data = data["Time Series (Daily)"]
    dates = get_two_days_before()
    values = []
    for date in dates:
        values.append(float(times_series_data[date]["4. close"]))

    diff_stocks = (values[0] - values[1]) / values[1]
    return diff_stocks


def check_amount(difference: float):
    """Check to see if amount change beyond 5%"""
    if abs(difference) > 0.05:
        print("Get News")
        return if_positive(difference)
    else:
        print("NOT Get News")
        return if_positive(difference)


def if_positive(difference: float):
    """If difference inceased"""
    return difference, difference > 0


## STEP 1: Use https://www.alphavantage.co
api_key_stock = os.environ.get("API_KEY_ALPHA_STOCK")
param_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": api_key_stock,
}
url = "https://www.alphavantage.co/query"
stock_response = requests.get(url, params=param_stock)
stock_response.raise_for_status()
stock_data = stock_response.json()

results = check_amount(get_diference_stocks(stock_data))


## STEP 2: Use https://newsapi.org
# TODO: Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
news_api_key = os.environ.get("API_KEY_NEWS")
news_url = "https://newsapi.org/v2/everything"
news_param = {
    "q": COMPANY_NAME,
    "sortBy": "publishedAt",
    "apiKey": news_api_key,
}
news_response = requests.get(news_url, params=news_param)
news_response.raise_for_status()
news_data = news_response.json()
print(news_data)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
# with smtp.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(my_email, password=python_mail_password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs=my_email,
#         msg=f"Subject:Rain\n\nBring an Umbrella Fool!!",
#     )
