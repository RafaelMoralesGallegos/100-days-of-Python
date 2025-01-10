import random

from flask import Flask

NUMBER = random.randint(0, 9)

to_high = "https://media2.giphy.com/media/14tf9peZdntGxO/200.webp?cid=ecf05e47ow9pm49r39tils6236u2ok9tab4htkc4for94d63&ep=v1_gifs_search&rid=200.webp&ct=g"
to_low = "https://media1.giphy.com/media/JfLdIahamXQI0/200.webp?cid=790b761192obe65sa28zdl1m3h87y91pm7ab2lpx1zlfczqf&ep=v1_gifs_search&rid=200.webp&ct=g"
correct = "https://media0.giphy.com/media/G3NZ371qiaLks/giphy.webp?cid=ecf05e47ow9pm49r39tils6236u2ok9tab4htkc4for94d63&ep=v1_gifs_search&rid=giphy.webp&ct=g"

app = Flask(__name__)


def guess_option(function):
    def wrapped(*args, **kwargs):
        if kwargs["guess"] < NUMBER:
            html = (
                f"<h1 style='color:red; text-align: center'>"
                f"{function("Too Low, try again!")}</h1>"
                f"<p style='text-align: center'><img src={to_low}></p>"
            )
        elif kwargs["guess"] > NUMBER:
            html = (
                f"<h1 style='color:blue; text-align: center'>"
                f"{function("Too High, try again!")}</h1>"
                f"<p style='text-align: center'><img src={to_high}></p>"
            )
        else:
            html = (
                f"<h1 style='color:green; text-align: center'>{function("Correct!!!")}</h1>"
                f"<p style='text-align: center'><img src={correct}></p>"
            )

        return html

    return wrapped


@app.route("/")
def guess_number():
    return (
        "<h1 style='text-align: center'>Guess a number between 0 and 9</h1>"
        "<p style='text-align: center'>"
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'
        "</p>"
    )


@app.route("/<int:guess>")
@guess_option
def user_guess(text):
    return text


if __name__ == "__main__":
    print(NUMBER)
    app.run(debug=True)
