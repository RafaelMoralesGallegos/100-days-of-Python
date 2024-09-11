# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import datetime as dt
import os
import smtplib as smtp
import time

from dotenv import load_dotenv

from data_manager import DataManager
from flight_data import find_cheapest_flight
from flight_search import FlightSearch

load_dotenv()
my_email = os.environ.get("ULTRA_MAIL_MAIL")
python_mail_password = os.environ.get("ULTRA_MAIL_PASS")

IATA_CODE = "GDL"


def return_lowest_price(data: list):
    cheepest_flight = data[0]
    for flight in data:
        try:
            if flight.price < cheepest_flight.price:
                cheepest_flight = flight
        except TypeError:
            print("No flight plan")

    return cheepest_flight


def check_cheeper_flight(city, flight, data):
    try:
        if flight.price < city["lowestPrice"]:
            print(f"{city['city']}: ${flight.price}")
            # send_mail(flight)
            get_users_data(data, flight)
        else:
            print("Next City")
    except TypeError:
        print("Next City")


def get_users_data(data, flight):
    users = data.get_customer_email()
    for user in users:
        send_mail(flight, user["whatIsYourEmail"])


def send_mail(flight, user_email):
    with smtp.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password=python_mail_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=user_email,
            msg=(
                f"Subject:Lower Price Alert!\n\n"
                f"Only ${flight.price} to fly "
                f"from {flight.origin_airport} "
                f"to {flight.destination_airport}, "
                f"on {flight.out_date} "
                f"until {flight.return_date} "
                f"stops {flight.stops} "
            ),
        )
    print("email sent")


def main():
    sheet = DataManager()
    # sheet_data = sheet.get_from()
    sheet_data = [
        {"city": "Paris", "iataCode": "PAR", "lowestPrice": 30000, "id": 2},
        {"city": "Frankfurt", "iataCode": "FRA", "lowestPrice": 17000, "id": 3},
        {"city": "Tokyo", "iataCode": "TYO", "lowestPrice": 20000, "id": 4},
        {"city": "Hong Kong", "iataCode": "HKG", "lowestPrice": 20000, "id": 5},
        {"city": "Istanbul", "iataCode": "IST", "lowestPrice": 23000, "id": 6},
        {"city": "Kuala Lumpur", "iataCode": "KUL", "lowestPrice": 20000, "id": 7},
        {"city": "New York", "iataCode": "NYC", "lowestPrice": 5000, "id": 8},
        {"city": "San Francisco", "iataCode": "SFO", "lowestPrice": 5000, "id": 9},
        {"city": "Dublin", "iataCode": "DBN", "lowestPrice": 10000, "id": 10},
    ]
    flight_search = FlightSearch()
    sheet_data = flight_search.check_sheet_IATA(sheet_data)

    for city in sheet_data:
        print(f"Getting flights for {city['city']}...")
        flight_list = []
        for i in range(1, 30 + 1):
            tomorrow = dt.date.today() + dt.timedelta(days=i)
            return_date = tomorrow + dt.timedelta(days=7)
            flights = flight_search.find_cheep_flights(
                IATA_CODE, city["iataCode"], tomorrow, return_date
            )
            cheapest_flight = find_cheapest_flight(flights)
            time.sleep(2)

        flight_list.append(cheapest_flight)
        cheapest_flight = return_lowest_price(flight_list)
        if cheapest_flight.price == "N/A":
            print(
                f"No direct flight to {city['city']}. Looking for indirect flights..."
            )
            flight_list = []
            for i in range(1, 30 + 1):
                tomorrow = dt.date.today() + dt.timedelta(days=i)
                return_date = tomorrow + dt.timedelta(days=7)
                flights = flight_search.find_cheep_flights(
                    IATA_CODE, city["iataCode"], tomorrow, return_date, nonStop=False
                )
                cheapest_flight = find_cheapest_flight(flights)
                time.sleep(2)

        flight_list.append(cheapest_flight)
        cheapest_flight = return_lowest_price(flight_list)
        check_cheeper_flight(city, cheapest_flight, sheet)
        # Slowing down requests to avoid rate limit


if __name__ == "__main__":
    main()
    # if flights is None:
    #             flights = flight_search.find_cheep_flights(
    #                 IATA_CODE, city["iataCode"], tomorrow, return_date, nonStop=False
    #             )
