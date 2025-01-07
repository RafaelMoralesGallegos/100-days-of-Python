import os
import re
import time

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Load environment variables
load_dotenv()
SF_RENT_FORM = os.getenv("SF_RENT_FORM")
ZILLOW = os.getenv("ZILLOW_CLONE_URL")


def get_html() -> BeautifulSoup:
    response = requests.get(url=ZILLOW)  # type: ignore
    fake_wbsite = response.text
    soup = BeautifulSoup(fake_wbsite, "html.parser")

    return soup


def get_properties(soup: BeautifulSoup) -> list:
    address_list = soup.find_all("article", {"data-test": "property-card"})
    property_cards = [
        article.find("div", class_="StyledPropertyCardDataWrapper")
        for article in address_list
    ]

    return property_cards


def get_infomation(card: BeautifulSoup) -> tuple:
    address_info = card.find("address").text.strip()  # type: ignore
    new_address = remove_pipe_separator(address_info)
    property_url = card.find("a").get("href")  # type: ignore
    price = card.find("span", {"data-test": "property-card-price"}).text.strip()  # type: ignore
    new_price = remove_after_symbols(price)

    return new_address, property_url, new_price


def remove_pipe_separator(address_str: str) -> str:
    """Returns address in usable string format

    Args:
        address_str (str): address given by beautiful soup

    Returns:
        str: plane string of address now separated by only comas
    """
    return address_str.replace(" | ", ", ")


def remove_after_symbols(price: str) -> str:
    """Remove uncecessary additional sybols form price

    Args:
        price (str): price given by beautiful soup

    Returns:
        str: plane string of price with $ at the beginnig
    """
    return re.split(r"[+/]", price, maxsplit=1)[0]


class FromBot:

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)  # Keep the browser open

        # Set Chrome options
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)  # Keep the browser open

        # Initialize the driver with the options
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 30)


# Main execution
def main():
    soup = get_html()
    cards = get_properties(soup)
    property_info = [get_infomation(card) for card in cards]

    bot = FromBot()


if __name__ == "__main__":
    main()
