import os
import time

from dotenv import load_dotenv
from selenium import webdriver
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

        cookies = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='Not now']"))
        )
        cookies.click()

    def find_followers(self):
        self.driver.get("https://twitter.com/login")

    def follow(self):
        pass


# Main execution
def main():
    bot = IntagramBot()
    bot.login()
    bot.find_followers()
    bot.follow()
    # bot.perform_speed_test()
    # print(f"Download Speed: {bot.down} Mbps")
    # print(f"Upload Speed: {bot.up} Mbps")
    # if bot.down < PROMISED_DOWNLOAD or bot.up < PROMISED_UPLOAD:
    #     bot.post_complaint_on_twitter()
    # else:
    #     print("It's all good")
    # bot.driver.quit()


if __name__ == "__main__":
    main()
