from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def recive_data():
    return "Success! Form submitted"
    
if __name__  == "__main__":
    app.run(debug=True)
    
    