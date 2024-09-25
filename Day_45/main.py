# import lxml
from bs4 import BeautifulSoup

with open(r"website.html", "r") as file:
    website = file.read()

soup = BeautifulSoup(website, "html.parser")

# print(soup.title.string)
# print(soup.prettify())
