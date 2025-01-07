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
FORM = os.getenv("SF_RENT_FORM")
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
    property_url = card.find("a").get("href")  # type: ignore
    price = card.find("span", {"data-test": "property-card-price"}).text.strip()  # type: ignore
    new_price = remove_after_symbols(price)

    return address_info, property_url, new_price


def remove_after_symbols(price: str) -> str:
    return re.split(r"[+/]", price, maxsplit=1)[0]


# Main execution
def main():
    soup = get_html()
    cards = get_properties(soup)
    property_info = [get_infomation(card) for card in cards]


if __name__ == "__main__":
    main()
