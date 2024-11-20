import requests
import datetime as dt

# ---------------------------------------------------------------------------------------------------------------------
GENDER = "male"
WEIGHT_KG = 107
HEIGHT_CM = 186
AGE = 32
APP_ID = "***********"
API_KEY = ""***********""
username = ""***********""
GOOGLE_SHEET_NAME = "workoutTracking"
sheetName = "work"

# ---------------------------------------------------------------------------------------------------------------------
now = dt.datetime.now()
today_date = now.strftime("%d-%b-%Y")
today_time = now.strftime("%X")
print(today_date)
print(today_time)

# ---------------------------------------------------------------------------------------------------------------------
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(f"Nutritionix API call: \n {result} \n")

# ---------------------------------------------------------------------------------------------------------------------
sheet_endpoint = "https://api.sheety.co/6982e028f287459cfa82b99a58eba01c/workoutTracking/work"
bearer_headers = {
    "Authorization": "Bearer ***********"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        sheetName: {
            "date": today_date,
            "time": today_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    print(sheet_inputs)
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )

    print(f"Status Code: {sheet_response.status_code}")
