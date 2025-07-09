from flask import Flask, render_template, request
import requests
import os
import smtplib

from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file


EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
MY_EMAIL = os.getenv("MY_EMAIL")
api = 'https://api.npoint.io/2378d3d8e0262f7e23d3'


response = requests.get(api).json()


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', data=response)


@app.route('/about')
def click_about():
    return render_template('about.html')


@app.route('/contact', methods=["POST", "GET"])
def click_contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"],data["email"],data["phone"],data["message"])
        return render_template('contact.html', msg_sent= True)
    return render_template('contact.html', msg_sent= False)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs=MY_EMAIL,msg= email_message)
    

@app.route('/page/<int:n>')
def goto(n):
    cur_page = None
    for item in response:
        if item['id'] == n:
            cur_page = item
            return render_template('post.html', post=cur_page)




if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
