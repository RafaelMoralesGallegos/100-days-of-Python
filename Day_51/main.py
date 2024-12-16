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
TWITTER_EMAIL = os.getenv("EMAIL")
TWITTER_PASSWORD = os.getenv("PASSWORD")
TWITTER_NAME = os.getenv("TWITTER_NAME")

PROMISED_DOWNLOAD = 100
PROMISED_UPLOAD = 100
PROVIDER_HANDLE = "@totalplaymx"


class InternetSpeedTwitterBot:

    def __init__(self) -> None:
        # Initialize WebDriver
        # Set Chrome options
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)  # Keep the browser open

        # Initialize the driver with the options
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 30)

        self.down = 0
        self.up = 0

    def perform_speed_test(self):
        """Performs the speed test and returns download and upload speeds."""
        self.driver.get("https://www.speedtest.net/")
        go_button = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "start-text"))
        )
        go_button.click()

        # Wait for the test to complete
        time.sleep(60)  # Adjust based on your internet speed

        self.down = float(
            self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "download-speed"))
            ).text
        )
        self.up = float(self.driver.find_element(By.CLASS_NAME, "upload-speed").text)

    def post_complaint_on_twitter(self):
        """Logs into Twitter and posts a complaint tweet if speeds are below promised."""
        self.driver.get("https://twitter.com/login")

        # Log in
        email_input = self.wait.until(EC.presence_of_element_located((By.NAME, "text")))
        email_input.send_keys(TWITTER_EMAIL)  # type: ignore
        email_input.send_keys(Keys.RETURN)

        time.sleep(2)  # Wait for the next step

        twitter_name = self.wait.until(
            EC.presence_of_element_located((By.NAME, "text"))
        )
        twitter_name.send_keys(TWITTER_NAME)  # type: ignore
        twitter_name.send_keys(Keys.RETURN)

        time.sleep(2)  # Wait for the next step

        password_input = self.wait.until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_input.send_keys(TWITTER_PASSWORD)  # type: ignore
        password_input.send_keys(Keys.RETURN)

        # Wait for login to complete
        time.sleep(5)

        # Compose a tweet
        complaint = (
            f"Hey {PROVIDER_HANDLE}, I just ran a speed test and got {self.down} Mbps download "
            f"and {self.up} Mbps upload. This is far below the promised speeds of "
            f"{PROMISED_DOWNLOAD} Mbps download and {PROMISED_UPLOAD} Mbps upload. "
            f"Please resolve this issue immediately!"
        )

        tweet_box = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.public-DraftStyleDefault-block")
            )
        )
        ActionChains(self.driver).move_to_element(tweet_box).click().send_keys(
            complaint
        ).perform()

        # Send the tweet
        tweet_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@data-testid='tweetButtonInline']")
            )
        )
        tweet_button.click()


# Main execution
def main():
    bot = InternetSpeedTwitterBot()
    bot.perform_speed_test()
    print(f"Download Speed: {bot.down} Mbps")
    print(f"Upload Speed: {bot.up} Mbps")
    if bot.down < PROMISED_DOWNLOAD or bot.up < PROMISED_UPLOAD:
        bot.post_complaint_on_twitter()
    else:
        print("It's all good")
    bot.driver.quit()


if __name__ == "__main__":
    main()
