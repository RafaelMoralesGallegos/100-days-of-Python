# import lxml
from bs4 import BeautifulSoup

with open(r"website.html", "r") as file:
    website = file.read()

soup = BeautifulSoup(website, "html.parser")

# print(soup.title.string)
# print(soup.prettify())
# print(soup.p)

all_achor_tags = soup.find_all(name="a")
for tag in all_achor_tags:
    # print(tag.getText())
    # print(tag.get("href"))
    pass

heading = soup.find(name="h1", id="name")
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

company_url = soup.select_one(selector="p a")
# print(company_url)

name = soup.select(selector="#name")
# print(name)

headings = soup.select(".heading")
print(headings)
