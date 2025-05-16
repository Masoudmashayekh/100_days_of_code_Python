from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(0, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/<name>")
def age_gen(name):
    response_age = requests.get(url=f"https://api.agify.io/?name={name}")
    response_gender = requests.get(url=f"https://api.genderize.io?name={name}")
    age = response_age.json()["age"]
    gender = response_gender.json()["gender"]
    return render_template("page_1.html", age=age, gen=gender, name= name)


if __name__ == "__main__":
    app.run(debug=True)
