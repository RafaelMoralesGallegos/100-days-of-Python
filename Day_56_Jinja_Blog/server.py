import random
from datetime import date

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    year = date.today().year
    return render_template("index.html", number=random_number, year=year)


# Todo: Continue with Udemy code
if __name__ == "__main__":
    app.run(debug=True)
