import datetime as dt
import os
import time

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
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {"keyword": city_name, "max": "1", "include": "AIRPORTS"}
        response = requests.get(url=city_endpoint, headers=headers, params=query)
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

    def find_cheep_flights(self, origin_code, destination_code, from_time, to_time):
        """We're looking only for non stop flights,
        that leave anytime between tomorrow and in 6 months time.
        We're also looking for round trips for 1 adult.
        The currency of the price we get back should be in GBP.
        """

        flight_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": origin_code,
            "destinationLocationCode": destination_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "1",
        }
        response = requests.get(
            url=flight_endpoint,
            headers=headers,
            params=query,
        )
        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print(
                "There was a problem with the flight search.\n"
                "For details on status codes, check the API documentation:\n"
                "https://developers.amadeus.com/self-service/category/flights/api-doc/"
                "flight-offers-search/api-reference"
            )
            print("Response body:", response.text)
            return None

        return response.json()


if __name__ == "__main__":
    flich_search = FlightSearch()
    tomorrow = dt.date.today() + dt.timedelta(days=1)
    return_date = tomorrow + dt.timedelta(days=7)
    print(flich_search.find_cheep_flights("MEX", "PAR", tomorrow, return_date))
