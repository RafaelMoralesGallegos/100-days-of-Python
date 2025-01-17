import os

import email_validator
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

"""
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
"""
load_dotenv()
app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = os.environ["WTF_CSRF_SECRET_KEY"]

SECRET_EMAIL = "admin@email.com"
SECRET_PASSWORD = "12345678"


# create Flask_WTF class
class MyForm(FlaskForm):
    email = StringField(
        label="What is your Email?",
        validators=[DataRequired(), Length(min=6), Email()],
    )
    password = PasswordField(
        label="What is your Password?",
        validators=[DataRequired(), Length(min=8, max=12)],
    )
    submit = SubmitField(label="Log in")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        if validate_secrets(email, password):
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template("login.html", form=form)


def validate_secrets(email, password):
    """See if the email and password are the secret"""
    return email == SECRET_EMAIL and password == SECRET_PASSWORD


if __name__ == "__main__":
    app.run(debug=True)
