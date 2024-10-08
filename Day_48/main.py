from selenium import webdriver

# Keep Chrome open in browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com.mx/")

# To close driver
# driver.close()
# driver.quit()
