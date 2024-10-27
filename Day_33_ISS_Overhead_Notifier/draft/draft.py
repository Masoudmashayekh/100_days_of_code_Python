import requests
from datetime import datetime

MY_LAT = 45.184727
MY_LON = 9.158207
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # print(response)
# # print(response.status_code)
# print(response.raise_for_status())
# data = response.json()
# print(data)
# longitude = float(data["iss_position"]["longitude"])
# latitude = float(data["iss_position"]["latitude"])
# iss_position = (longitude, latitude)
# print(longitude)
# print(latitude)
# print(iss_position)
parameters = {
    "lat": MY_LAT,
    "lng": MY_LON,
    "formatted": 0
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data["results"]["sunrise"])
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

# print(sunrise.split("T"))
# print(sunrise.split("T")[1].split(":"))
# print(sunrise.split("T")[1].split(":")[0])
print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)
