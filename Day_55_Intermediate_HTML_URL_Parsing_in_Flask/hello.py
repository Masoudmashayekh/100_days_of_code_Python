from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"

    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"

    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"

    return wrapper


@app.route("/")
def hello_world():
    return '<h1 style="text-align:center">Hello, World!</h1>' \
           '<p style="text-align:center">This is my first Website.</p>' \
           '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ3I3Ymp2MzQ5amRkNmVyenB3aXUyY201OHozdmFtbzBmZmhoOXJwcSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3osxYoCkKu892JBLUc/giphy.gif" width=300>'


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "bye"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello {name}, you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)
