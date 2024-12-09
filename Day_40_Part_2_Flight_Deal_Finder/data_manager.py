import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/78f3528db14a6799e07862c5309cb5bf/flightPricesNow/sheet1"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/78f3528db14a6799e07862c5309cb5bf/flightPricesNow/users"


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.customer_data = {}

    def get_data_google_sheet(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        self.destination_data = response.json()
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "sheet1": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )

    def get_customer_emails(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
