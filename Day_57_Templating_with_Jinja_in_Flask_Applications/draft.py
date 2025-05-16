import requests


name = input()
response_age = requests.get(url=f"https://api.agify.io/?name={name}")
response_gender = requests.get(url=f"https://api.genderize.io?name={name}")

print(response_age.json())
print(response_gender.json())