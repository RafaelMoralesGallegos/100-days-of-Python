import os

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

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
app.config["SECRET_KEY"] = os.environ["WTF_CSRF_SECRET_KEY"]
print(os.environ["WTF_CSRF_SECRET_KEY"])


@app.route("/")
def home():
    return render_template("index.html")


# create Flask_WTF class
class MyForm(FlaskForm):
    email = StringField("What is your Email?", validators=[DataRequired()])
    password = StringField("What is your Password?", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        name = form.email.data
        form.email.data = ""
        password = form.password.data
        form.password.data = ""

    return render_template("login.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
