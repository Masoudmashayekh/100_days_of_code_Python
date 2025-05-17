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


@app.route("/guess/<name>")
def guess(name):
    response_age = requests.get(url=f"https://api.agify.io/?name={name}")
    response_gender = requests.get(url=f"https://api.genderize.io?name={name}")
    age = response_age.json()["age"]
    gender = response_gender.json()["gender"]
    return render_template("guess.html", age=age, gen=gender, name= name)


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_url)
    all_post = response.json()
    return render_template("blog.html", posts=all_post)

if __name__ == "__main__":
    app.run(debug=True)
