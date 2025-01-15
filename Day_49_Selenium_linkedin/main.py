import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Load environment variables
load_dotenv()
email = os.getenv("LINKEDIN_EMAIL")
password = os.getenv("LINKEDIN_PASSWORD")

# Set up WebDriver with options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(
        by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn"
    )[1]
    discard_button.click()


try:
    # Open LinkedIn
    driver.get("https://www.linkedin.com/login")

    # Log in
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    ).send_keys(
        email  # type: ignore
    )
    driver.find_element(By.ID, "password").send_keys(password + Keys.RETURN)  # type: ignore

    # Navigate to Jobs
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Jobs"))
    ).click()

    # Search for "Python Developer" in "Zapopan, Jalisco, Mexico"
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input.jobs-search-box__text-input")
        )
    )
    search_fields = driver.find_elements(
        By.CSS_SELECTOR, "input.jobs-search-box__text-input"
    )
    search_fields[0].send_keys("Python Developer" + Keys.RETURN)  # Job title
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@aria-label='Easy Apply filter.']")
        )
    ).click()
    time.sleep(5)
    apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
    apply_button.click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@aria-label='Continue to next step']")
        )
    ).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@aria-label='Continue to next step']")
        )
    ).click()
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
    if submit_button.get_attribute("data-control-name") == "continue_unify":
        abort_application()
        print("Complex application, skipped.")
    else:
        # Click Submit Button
        print("Submitting job application")
        submit_button.click()
    # driver.find_element(By.XPATH, "//button[contains(text(), 'Show results')]").click()

    print("Search completed with Easy Apply filter.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Optional: Keep the browser open or close after completion
    # driver.quit()  //button[span='All filters']
    pass
