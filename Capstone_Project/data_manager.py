import os

import requests
from dotenv import load_dotenv

load_dotenv()


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.api_endpoint = os.environ.get("FLIGHT_DEALS_SHEETY_ENDPOINT")
        self.api_user_endpoint = os.environ.get("USERS_SHEETY_ENDPOINT")
        self.api_authorize = os.environ.get("FLIGHT_DEALS_SHEETY_AUTH")
        self.api_headers = {"Authorization": self.api_authorize}

    def get_from(self) -> list:
        """Return all the Rows brom the prices sheet"""
        response = requests.get(url=self.api_endpoint, headers=self.api_headers)
        sheet_rows = response.json()
        return sheet_rows["prices"]

    def put_towards(self, data: dict) -> None:
        """Modify the rows in Google Sheet"""
        {"city": "Paris", "iataCode": "TESTING", "lowestPrice": 54, "id": 2}
        parameters = {
            "price": {
                "city": data["city"],
                "iataCode": data["iataCode"],
                "lowestPrice": data["lowestPrice"],
            }
        }
        requests.put(
            url=f"{self.api_endpoint}/{data["id"]}",
            headers=self.api_headers,
            json=parameters,
        )

    def get_customer_email(self):
        response = requests.get(url=self.api_user_endpoint, headers=self.api_headers)
        data = response.json()
        customer_data = data["users"]
        return customer_data


if __name__ == "__main__":
    excel_sheet = DataManager()
    data = excel_sheet.get_customer_email()
    print(data)
