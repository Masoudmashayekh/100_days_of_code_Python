import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 45.184727
MY_LON = 9.158207
MY_EMAIL = "XXXXXXXX@gmail.com"
PASSWORD = "XXXXXXXX"


# ISS 
def is_iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_data = iss_response.json()
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LON - 5 <= iss_longitude <= MY_LON + 5:
        return True


# Sun 
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LON,
        "formatted": 0
    }
    sun_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    sun_data = sun_response.json()
    sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


# email me to tell me to look up
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="ZZZZZZZZ@gmail.com",
                                msg="Subject:Look Up👆🏻\n\nThe ISS is above you in the sky.")


