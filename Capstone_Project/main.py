# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import datetime as dt
import time

from data_manager import DataManager
from flight_data import find_cheapest_flight
from flight_search import FlightSearch

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


def main():
    # sheet = DataManager()
    # sheet_data = sheet.get_from()
    sheet_data = [
        {"city": "Paris", "iataCode": "PAR", "lowestPrice": 54, "id": 2},
        {"city": "Frankfurt", "iataCode": "FRA", "lowestPrice": 42, "id": 3},
        {"city": "Tokyo", "iataCode": "TYO", "lowestPrice": 485, "id": 4},
        {"city": "Hong Kong", "iataCode": "HKG", "lowestPrice": 551, "id": 5},
        {"city": "Istanbul", "iataCode": "IST", "lowestPrice": 95, "id": 6},
        {"city": "Kuala Lumpur", "iataCode": "KUL", "lowestPrice": 414, "id": 7},
        {"city": "New York", "iataCode": "NYC", "lowestPrice": 240, "id": 8},
        {"city": "San Francisco", "iataCode": "SFO", "lowestPrice": 260, "id": 9},
        {"city": "Dublin", "iataCode": "DBN", "lowestPrice": 378, "id": 10},
    ]
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
        print(f"{city['city']}: £{cheapest_flight.price}")
        # Slowing down requests to avoid rate limit
        time.sleep(2)


if __name__ == "__main__":
    main()
