import os
import time

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
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
INSTAGRAM_SIMILAR = os.getenv("INSTAGRAM_SIMILAR")


class IntagramBot:

    def __init__(self):
        # Initialize WebDriver
        # Set Chrome options
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)  # Keep the browser open

        # Initialize the driver with the options
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 30)

    def login(self):
        """Logs to Instagram using account"""
        self.driver.get("https://www.instagram.com/")

        # Log in
        email_input = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@aria-label='Phone number, username, or email']")
            )
        )
        email_input.send_keys(EMAIL)  # type: ignore

        password_input = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@aria-label='Password']")
            )
        )
        password_input.send_keys(PASSWORD)  # type: ignore

        time.sleep(2)

        log_in_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
        )
        log_in_button.click()

        not_now = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='Not now']"))
        )
        not_now.click()

    def find_followers(self):
        """Find followers of the similar Instagram account"""
        self.driver.get(INSTAGRAM_SIMILAR)  # type: ignore

        time.sleep(3)

        # Followers
        followers = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[text()=' followers']"))
        )
        followers.click()

        time.sleep(3)
        # Wait for the popup to appear
        self.scr1 = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]",
                )
            )
        )
        # Scroll to the bottom of the popup
        last_height = self.driver.execute_script(
            "return arguments[0].scrollHeight", self.scr1
        )
        while True:
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", self.scr1
            )
            # time.sleep(1.5)  # Wait for new content to load

            new_height = self.driver.execute_script(
                "return arguments[0].scrollHeight", self.scr1
            )
            if new_height == last_height:
                break  # Stop scrolling if no new followers load
            else:
                last_height = new_height

        print("Finished scrolling through the followers list.")

    def follow(self):
        # Check and update the (CSS) Selector for the "Follow" buttons as required.
        time.sleep(2)
        follow_buttons = self.driver.find_elements(
            By.XPATH, '//button[.//div/div[text()="Follow"]]'
        )

        for button in follow_buttons:
            try:
                button.click()
                print("Clicked a Follow button")
                time.sleep(2)  # Add delay
            except Exception as e:
                print(f"Error clicking button: {e}")

        print("Finished clicking all Follow buttons.")


# Main execution
def main():
    bot = IntagramBot()
    bot.login()
    bot.find_followers()
    bot.follow()
    bot.driver.quit()


if __name__ == "__main__":
    main()
