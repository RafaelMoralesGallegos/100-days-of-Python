import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
yc_website = response.text
soup = BeautifulSoup(yc_website, "html.parser")

titles_atributes = soup.find_all(name="h3", class_="title")
titles = []

for title in reversed(titles_atributes):
    titles.append(title.getText())

print(titles)
