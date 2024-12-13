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


def login_to_tinder(driver):
    driver.get("https://tinder.com")
    wait = WebDriverWait(driver, 20)

    # Click "Log In"
    login_button = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class, 'lxn9zzn') and text()='Log in']",
            )
        )
    )
    login_button.click()

    # Select Google login
    google_login = wait.until(EC.element_to_be_clickable((By.ID, "q-1115063307")))
    google_login.click()

    # Switch to Google login window
    driver.switch_to.window(driver.window_handles[1])

    # Enter Google email
    email_input = wait.until(EC.presence_of_element_located((By.ID, "identifierId")))
    email_input.send_keys(EMAIL)  # type: ignore
    email_input.send_keys(Keys.RETURN)
    time.sleep(2)

    # Enter Google password
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "Passwd")))
    password_input.send_keys(PASSWORD)  # type: ignore
    password_input.send_keys(Keys.RETURN)

    # Switch back to Tinder window
    driver.switch_to.window(driver.window_handles[0])

    # Allow time for login process to complete
    time.sleep(5)
    allow_loction = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='allow']"))
    )
    allow_loction.click()
    cookies = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class, 'lxn9zzn') and text()='I accept']",
            )
        )
    )
    cookies.click()
    notify_me = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='decline']"))
    )
    notify_me.click()
    time.sleep(5)


def swipe_right(driver):
    time.sleep(2)
    try:
        # Find and click the "Like" button
        # Locate the element
        like_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//*[@id='main-content']/div[1]/div/div/div/div[1]/div/div/div[4]/div/div[4]/button",
                )
            )
        )
        # Click the element
        like_button.click()

    except Exception as e:
        print(f"Error swiping: {e}")


def handle_match_popup(driver):
    try:
        # If a match occurs, handle the popup
        match_popup = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(text(), 'Continue to Tinder')]")
            )
        )
        match_popup.click()
    except:
        pass  # No match popup


def main():
    # Set Chrome options
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)  # Keep the browser open

    # Initialize the driver with the options
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    try:
        login_to_tinder(driver)

        # Swipe 100 times
        for _ in range(100):
            swipe_right(driver)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Comment out for testing
        # driver.quit()
        pass


if __name__ == "__main__":
    main()
