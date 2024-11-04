from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome open in browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# *346
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

# print(f"Price is ${price_dollar.text}.{price_cents.text}")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documentation_link = driver.find_element(
#     By.CSS_SELECTOR, value=".documentation-widget a"
# )
# print(documentation_link.text)
# bug_link = driver.find_element(
#     By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a'
# )
# print(bug_link.text)
# To close driver
# driver.close()
# time = driver.find_elements(
#     By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/time'
# )
# text = driver.find_elements(
#     By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/a'
# )

# * 347
section = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li")

update_dict = {
    i: {
        "time": element.find_element(By.TAG_NAME, value="time").text,
        "name": element.find_element(By.TAG_NAME, value="a").text,
    }
    for i, element in enumerate(section)
}
print(update_dict)

driver.quit()
