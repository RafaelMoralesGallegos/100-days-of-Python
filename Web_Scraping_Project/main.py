import os
import time

import requests
from bs4 import BeautifulSoup
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


def get_infomation():
    pass


# Main execution
def main():
    soup = get_html()
    cards = get_properties(soup)
    for card in cards:
        print(type(card))


if __name__ == "__main__":
    main()
