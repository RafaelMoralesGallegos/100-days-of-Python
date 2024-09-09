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

IATA_CODE = "MEX"


def return_lowest_price(data: list):
    cheepest_flight = data[0]
    for flight in data:
        try:
            if flight.price < cheepest_flight.price:
                cheepest_flight = flight
        except TypeError:
            print("No flight plan")

    return cheepest_flight


def check_cheeper_flight(city, flight):
    if flight.price < city["lowestPrice"]:
        print(f"{city['city']}: ${flight.price}")
        send_mail(flight)
    else:
        print("Next City")


def send_mail(flight):
    with smtp.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password=python_mail_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=(
                f"Subject:Lower Price Alert!\n\n"
                f"Only ${flight.price} to fly "
                f"from {flight.origin_airport} "
                f"to {flight.destination_airport}, "
                f"on {flight.out_date} "
                f"until {flight.return_date}"
            ),
        )
    print("email sent")


def main():
    sheet = DataManager()
    sheet_data = sheet.get_from()
    # sheet_data = [
    #     {"city": "Paris", "iataCode": "PAR", "lowestPrice": 1050, "id": 2},
    #     {"city": "Frankfurt", "iataCode": "FRA", "lowestPrice": 576, "id": 3},
    #     {"city": "Tokyo", "iataCode": "TYO", "lowestPrice": 780, "id": 4},
    #     {"city": "Hong Kong", "iataCode": "HKG", "lowestPrice": 650, "id": 5},
    #     {"city": "Istanbul", "iataCode": "IST", "lowestPrice": 780, "id": 6},
    #     {"city": "Kuala Lumpur", "iataCode": "KUL", "lowestPrice": 780, "id": 7},
    #     {"city": "New York", "iataCode": "NYC", "lowestPrice": 200, "id": 8},
    #     {"city": "San Francisco", "iataCode": "SFO", "lowestPrice": 230, "id": 9},
    #     {"city": "Dublin", "iataCode": "DBN", "lowestPrice": 576, "id": 10},
    # ]
    flich_search = FlightSearch()
    sheet_data = flich_search.check_sheet_IATA(sheet_data)

    for city in sheet_data:
        print(f"Getting flights for {city['city']}...")
        flight_list = []
        for i in range(1, 30 + 1):
            tomorrow = dt.date.today() + dt.timedelta(days=i)
            return_date = tomorrow + dt.timedelta(days=7)
            flights = flich_search.find_cheep_flights(
                IATA_CODE, city["iataCode"], tomorrow, return_date
            )
            cheapest_flight = find_cheapest_flight(flights)
            flight_list.append(cheapest_flight)

        cheapest_flight = return_lowest_price(flight_list)
        check_cheeper_flight(city, cheapest_flight)
        # Slowing down requests to avoid rate limit
        time.sleep(2)


if __name__ == "__main__":
    main()
