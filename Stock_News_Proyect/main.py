import datetime as dt
import os
import smtplib as smtp
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests
from pandas.tseries.offsets import BDay

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

my_email = "ultratumba25@gmail.com"
python_mail_password = os.environ.get("MAIL_PASS")
yesterday = ""


# Functions
def get_two_days_before():
    """Get the 2 Buissness days before"""
    global yesterday

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
        values = if_positive(difference)
        news = set_news_usabe(get_three_news())
        send_email(news, values)
    else:
        values = if_positive(difference)
        values = if_positive(difference)
        news = set_news_usabe(get_three_news())
        send_email(news, values)


def if_positive(difference: float):
    """If difference inceased"""
    return difference, difference > 0


def get_three_news():
    news_api_key = os.environ.get("API_KEY_NEWS")
    news_url = "https://newsapi.org/v2/everything"
    news_param = {
        "q": COMPANY_NAME,
        "from": yesterday,
        "to": yesterday,
        "sortBy": "popularity",
        "apiKey": news_api_key,
        "pageSize": 3,
    }
    news_response = requests.get(news_url, params=news_param)
    news_response.raise_for_status()
    news_data = news_response.json()
    return news_data


def send_email(data, values):
    msg = MIMEMultipart()
    msg["From"] = my_email
    msg["To"] = my_email
    msg["Subject"] = f"TSLA: {round(values[0]*100)}%"

    # Attach the text body to the email message
    msg.attach(MIMEText(data, "plain", "utf-8"))

    with smtp.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, password=python_mail_password)
        connection.send_message(msg)


def set_news_usabe(news):
    news_print = " "
    for article in news["articles"]:
        news_print += (
            f"Headline: {article["title"]}\n"
            f"Brief: {article["description"]}\n"
            f"URL: {article["url"]}\n\n"
        )
    return news_print


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
