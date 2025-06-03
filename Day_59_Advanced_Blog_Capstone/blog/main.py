from flask import Flask, render_template
import requests


api = 'https://api.npoint.io/2378d3d8e0262f7e23d3'


response = requests.get(api).json()


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', data=response)


@app.route('/about')
def click_about():
    return render_template('about.html')


@app.route('/contact')
def click_contact():
    return render_template('contact.html')


@app.route('/page/<int:n>')
def goto(n):
    cur_page = None
    for item in response:
        if item['id'] == n:
            cur_page = item
            return render_template('post.html', post=cur_page)


if __name__ == '__main__':
    app.run(debug=True)