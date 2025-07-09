from flask import Flask, render_template, request


app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def recive_data():
    username = request.form["username"]
    password = request.form["password"]
    return f"<h1>Name: {username} with pass: {password}</h1>"
    
if __name__  == "__main__":
    app.run(debug=True)
    
    