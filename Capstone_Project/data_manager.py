import os


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.api_endpoint = os.environ.get("FLIGHT_DEALS_SHEETY_ENDPOINT")
        self.api_authorize = os.environ.get("FLIGHT_DEALS_SHEETY_AUTH")


if __name__ == "__main__":
    print(True)
