import random
from datetime import date

import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    year = date.today().year
    # *Use kwags functionally to pass variables to html
    return render_template("index.html", number=random_number, year=year)


def get_age(name: str):
    """Get the age according to Agify

    Args:
        name (str): give the name

    Returns:
        int: number of data if api succesful, False if not
    """
    try:
        parameters = {"name": name}
        response = requests.get(url="https://api.agify.io?", params=parameters)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching agify data: {e}")
        return False
    else:
        data = response.json()
        return int(data["age"])


if __name__ == "__main__":
    # app.run(debug=True)
    name = input("give me name: ")
    age = get_age(name)
