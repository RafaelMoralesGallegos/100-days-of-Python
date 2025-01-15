import os

import requests
import spotipy
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()


date = input("Which date do you want to travel to? Type date in format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{date}/"


def spotify_auto():
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="http://example.com",
            client_id=os.environ.get("CLIENT_ID_SPOTIFY"),
            client_secret=os.environ.get("CLIENT_SECRET_SPOTIFY"),
            show_dialog=True,
            cache_path="token.txt",
            username=os.environ.get("SPOTIFY_USERNAME"),
        )
    )
    return sp


def main():
    response = requests.get(URL)
    billboard_hot = response.text
    soup = BeautifulSoup(billboard_hot, "html.parser")

    titles = soup.select("li ul li h3")
    song_names = [title.getText().strip() for title in titles]
    sp = spotify_auto()
    user_id = sp.current_user()["id"]

    song_uris = []
    year = date.split("-")[0]
    for song in song_names:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")

    # Creating a new private playlist in Spotify
    playlist = sp.user_playlist_create(
        user=user_id, name=f"{date} Billboard 100", public=False
    )
    # Adding songs found into the new playlist
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)


if __name__ == "__main__":
    main()
