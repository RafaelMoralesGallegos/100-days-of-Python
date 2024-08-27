import os

import requests
from dotenv import load_dotenv

from data_manager import DataManager

load_dotenv()


class FlightSearch:
    def __init__(self) -> None:
        """This class is responsible for talking to the Flight Search API."""
        self.data_manager = DataManager()
        self._api_secret = os.environ.get("AMADEUS_API_SECRET")
        self._api_key = os.environ.get("AMADEUS_API_KEY")
        self._token = self._get_new_token()

    def check_sheet_IATA(self, data: list) -> list:
        """Add IATA values to d"""
        for city in data:
            if city["iataCode"] == "":
                city["iataCode"] = self._get_city_IATA(city["city"])
                self.data_manager.put_towards(city)

        return data

    def _get_new_token(self):
        """Generates the authentication token
        used for accessing the Amadeus API and returns it
        Returns:
            str: The new access token obtained from the API response.
        """
        token_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
        header = {"Content-Type": "application/x-www-form-urlencoded"}
        body = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret,
        }
        response = requests.post(url=token_endpoint, headers=header, data=body)

        return response.json()["access_token"]

    def _get_city_IATA(self, city_name: str) -> str:
        """Generates an API Post request and get the IATA code from
        each city/ of an AIRPORT.
        Returns:
            str: Code given by IATA of the city and Airport
        """
        city_endpoint = (
            "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        )
        header = {"Authorization": f"Bearer {self._token}"}
        query = {"keyword": city_name, "max": "1", "include": "AIRPORTS"}
        response = requests.get(url=city_endpoint, headers=header, params=query)
        try:
            code = response.json()["data"][0]["iataCode"]
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"
        else:
            return code


if __name__ == "__main__":
    flight = FlightSearch()
    flight._get_city_IATA("Paris")
