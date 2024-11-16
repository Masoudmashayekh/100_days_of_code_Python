import requests
import datetime as dt

QUANTITY = "4.0"
GRAPH_ID = "graph1"
USERNAME = "secret"
TOKEN = "secret"
PIXELA_END_POINT = "https://pixe.la/v1/users"

# ---------------------------------------------------------------------------------------------------------------------
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=PIXELA_END_POINT, json=user_params)
# print(response.text)

# ---------------------------------------------------------------------------------------------------------------------
graph_endpoint = f"{PIXELA_END_POINT}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hour",
    "type": "float",
    "color": "shibafu",
}

header = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint,json=graph_config, headers= header)
# print(response.text)
# https://pixe.la/v1/users/USERNAME/graphs/graph1.html

# ---------------------------------------------------------------------------------------------------------------------
post_pixel_endpoint = f"{PIXELA_END_POINT}/{USERNAME}/graphs/{GRAPH_ID}"
today = dt.datetime.now()
yyyyMMdd = today.strftime("%Y%m%d")


pixel_params = {"date": yyyyMMdd,
                "quantity": QUANTITY
                }

post_pixel_response = requests.post(url=post_pixel_endpoint,json=pixel_params,headers=header)
print(post_pixel_response.text)

# ---------------------------------------------------------------------------------------------------------------------
put_params = {"quantity": QUANTITY}
put_endpoint = f"{PIXELA_END_POINT}/{USERNAME}/graphs/{GRAPH_ID}/{yyyyMMdd}"
# put_response = requests.put(url=put_endpoint,json=put_params,headers=header)
# print(put_response.text)

# ---------------------------------------------------------------------------------------------------------------------
# delete_endpoint = f"{PIXELA_END_POINT}/{USERNAME}/graphs/{GRAPH_ID}/{yyyyMMdd}"
# response = requests.delete(url=delete_endpoint,headers= header)
# print(response.text)
