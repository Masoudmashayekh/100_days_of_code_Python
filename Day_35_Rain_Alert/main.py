import os
import requests
from twilio.rest import Client

# Constants -----------------------------------------------------------------------------------------------------------
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("API_KEY")
weather_params = {
    "lat": 45.184727,
    "lon": 9.158207,
    "appid": api_key,
    "cnt": 4,
}

account_sid = os.environ.get("A_SID")
auth_token = os.environ.get("AUTH_TOKEN")
USER = "+000000000000"

# -----------------------------------------------------------------------------------------------------------------
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
print(f"Status: {response.status_code}")
weather_data = response.json()
print(weather_data)
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"It's going to rain today. Remember to bring an Umbrella☔️",
        from_="+12174724154",
        to= USER
    )
    print(message.status)
    message_W = client.messages.create(
        body="It is going to rain today. Remember to bring an Umbrella☔️",
        from_='whatsapp:+14155238886',
        to=f'whatsapp:{USER}'
    )
    print(message_W.status)
