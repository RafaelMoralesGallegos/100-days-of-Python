from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome open in browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.ID, "articlecount").find_element(
    By.TAG_NAME, "a"
)
print(article_count.text)

driver.quit()
