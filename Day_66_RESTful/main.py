import random as rd

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

"""
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
"""

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    random_num = rd.randint(1, Cafe.query.count())
    rand_cafe: Cafe = Cafe.query.get(random_num)  # type: ignore

    cafe = json_cafe(rand_cafe)
    return jsonify({"cafes": cafe})


@app.route("/all")
def get_all_cafe():
    all_cafes = Cafe.query.all()
    cafes = [json_cafe(cafe) for cafe in all_cafes]

    return jsonify({"cafes": cafes})


@app.route("/search")
def search():
    loc = request.args.get("loc")
    search_cafe = Cafe.query.where(Cafe.location == loc).all()
    if search_cafe:
        cafes = [json_cafe(cafe) for cafe in search_cafe]
        return jsonify({"cafes": cafes})
    else:
        return jsonify(
            {"error": {"Not Found": "Sorry, we don't have a cafe at that location"}}
        )


def json_cafe(cafe: Cafe) -> dict:
    cafe_dict = {
        # "id": cafe.id,
        "name": cafe.name,
        "map_url": cafe.map_url,
        "img_url": cafe.img_url,
        "location": cafe.location,
        "seats": cafe.seats,
        "coffee_price": cafe.coffee_price,
        "amenities": {
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
        },
    }

    return cafe_dict


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def post_new_cafe():
    cafe = Cafe(
        name=request.form.get("name"),  # type: ignore
        map_url=request.form.get("map_url"),  # type: ignore
        img_url=request.form.get("img_url"),  # type: ignore
        location=request.form.get("loc"),  # type: ignore
        seats=request.form.get("seats"),  # type: ignore
        has_toilet=bool(request.form.get("toilet")),  # type: ignore
        has_wifi=bool(request.form.get("wifi")),  # type: ignore
        has_sockets=bool(request.form.get("sockets")),  # type: ignore
        can_take_calls=bool(request.form.get("calls")),  # type: ignore
        coffee_price=request.form.get("coffee_price"),  # type: ignore
    )
    db.session.add(cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == "__main__":
    app.run(debug=True)
