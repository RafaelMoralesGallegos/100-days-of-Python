import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
NEW_URL = "https://www.empireonline.com/movies/features/best-movies-2/"


# Write your code below this line 👇
def old_code():
    response = requests.get(URL)
    archive_website = response.text
    soup = BeautifulSoup(archive_website, "html.parser")

    titles_atributes = soup.find_all(name="h3", class_="title")
    titles = [title.getText() for title in reversed(titles_atributes)]

    with open("100_movies/Old_Movies.txt", "w", encoding="utf-8") as file:
        for title in titles:
            file.write(f"{title}\n")


def new_code():
    response = requests.get(NEW_URL)
    empire_website = response.text
    soup = BeautifulSoup(empire_website, "html.parser")

    atr_h3 = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
    titles = [title.getText() for title in reversed(atr_h3)]

    with open("100_movies/New_Movies.txt", "w", encoding="utf-8") as file:
        for title in titles:
            file.write(f"{title}\n")


old_code()
new_code()
