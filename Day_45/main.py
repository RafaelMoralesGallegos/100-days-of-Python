from bs4 import BeautifulSoup

with open(r"website.html", "r") as file:
    website = file.read()

print(website)
