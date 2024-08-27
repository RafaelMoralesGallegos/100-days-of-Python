# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager


def main():
    sheet = DataManager()
    sheet_data = sheet.get_from()
    print(sheet_data)


if __name__ == "__main__":
    main()
