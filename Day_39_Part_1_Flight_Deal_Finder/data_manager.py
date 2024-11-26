import requests

SHEETY_PRICES_ENDPOINT = "private"


class DataManager:

    def __init__(self):
        self.destination_data = {}

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
