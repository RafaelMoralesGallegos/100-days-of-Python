from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Keep Chrome open in browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# *Testing Web
# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element(By.ID, "articlecount").find_element(
#     By.TAG_NAME, "a"
# )
# print(article_count.text)
# article_count.click()
# content_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# content_portals.click()
# driver.quit()


# Wait for the element to be clickable
# search_bar = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.NAME, "search"))
# )
# search_bar.click()
# search_bar.send_keys("Python", Keys.ENTER)


# search_butt = driver.find_element(By.CSS_SELECTOR, "#searchform button")
# search_butt.click()

# *Challenge
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

entry_fname = driver.find_element(By.NAME, value="fName")
entry_fname.send_keys("Rafael")
entry_lname = driver.find_element(By.NAME, value="lName")
entry_lname.send_keys("Morales")
entry_email = driver.find_element(By.NAME, value="email")
entry_email.send_keys("rafael.morales@email.com", Keys.ENTER)
