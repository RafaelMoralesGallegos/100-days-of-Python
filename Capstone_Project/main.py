# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch


def main():
    sheet = DataManager()
    sheet_data = sheet.get_from()
    # sheet_data = [
    #     {"city": "Paris", "iataCode": "TESTING", "lowestPrice": 54, "id": 2},
    #     {"city": "Frankfurt", "iataCode": "TESTING", "lowestPrice": 42, "id": 3},
    #     {"city": "Tokyo", "iataCode": "TESTING", "lowestPrice": 485, "id": 4},
    #     {"city": "Hong Kong", "iataCode": "TESTING", "lowestPrice": 551, "id": 5},
    #     {"city": "Istanbul", "iataCode": "TESTING", "lowestPrice": 95, "id": 6},
    #     {"city": "Kuala Lumpur", "iataCode": "TESTING", "lowestPrice": 414, "id": 7},
    #     {"city": "New York", "iataCode": "TESTING", "lowestPrice": 240, "id": 8},
    #     {"city": "San Francisco", "iataCode": "TESTING", "lowestPrice": 260, "id": 9},
    #     {"city": "Dublin", "iataCode": "TESTING", "lowestPrice": 378, "id": 10},
    # ]
    flich_search = FlightSearch()
    sheet_data = flich_search.check_sheet_IATA(sheet_data)
    print(sheet_data)


if __name__ == "__main__":
    main()
