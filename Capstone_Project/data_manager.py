import os

import requests
from dotenv import load_dotenv

load_dotenv()


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.api_endpoint = os.environ.get("FLIGHT_DEALS_SHEETY_ENDPOINT")
        self.api_authorize = os.environ.get("FLIGHT_DEALS_SHEETY_AUTH")
        self.api_headers = {"Authorization": self.api_authorize}

    def get_from(self) -> dict:
        response = requests.get(url=self.api_endpoint, headers=self.api_headers)
        sheet_rows = response.json()
        return sheet_rows["prices"]


if __name__ == "__main__":
    excel_sheet = DataManager()
    excel_sheet.get_from()
