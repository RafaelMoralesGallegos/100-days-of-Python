import requests
from bs4 import BeautifulSoup

date = input("Which date do you want to travel to? Type date in format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{date}/"


def main():
    response = requests.get(URL)
    billboard_hot = response.text
    soup = BeautifulSoup(billboard_hot, "html.parser")

    titles = soup.select("li ul li h3")
    song_names = [title.getText().strip() for title in titles]


if __name__ == "__main__":
    main()
