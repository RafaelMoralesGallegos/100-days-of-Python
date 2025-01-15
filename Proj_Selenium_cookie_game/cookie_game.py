import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Keep Chrome open in browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# *Challenge
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")


def upgrade():
    for i in range(9):
        try:
            upgrade = driver.find_element(By.ID, value=f"upgrade{i}")
            if upgrade.get_attribute("class") == "crate upgrade enabled":
                upgrade.click()
        except:
            pass


def click_big_cookie():
    big_cookie = driver.find_element(By.ID, value="bigCookie")
    end_time = time.time() + 5
    while time.time() < end_time:
        big_cookie.click()

    upgrade()
    try_product()


def try_product():
    for i in reversed(range(8)):
        try:
            product = driver.find_element(By.ID, f"product{i}")
            if product.get_attribute("class") == "product unlocked enabled":
                product.click()
                try_product()
        except:
            pass


def find_cookie_second():
    cookie_second = driver.find_element(By.ID, value="cookiesPerSecond")
    print(f"Cookies {cookie_second.text}")


time.sleep(3)
language = driver.find_element(By.ID, value="langSelect-EN")
language.click()

time.sleep(3)
end_time = time.time() + 60 * 5
while time.time() < end_time:
    click_big_cookie()

find_cookie_second()
