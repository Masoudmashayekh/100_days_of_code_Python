import requests
from twilio.rest import Client
import os

# -----(Constants)-------------------------------------------------------------------------------------------------------
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

news_params = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]

iterator = iter(data.items())
yesterday_date, yesterday_date_data = next(iterator)
day_before_yesterday_date, day_before_yesterday_date_data = next(iterator)
price_yesterday = float(yesterday_date_data["4. close"])
price_day_before_yesterday = float(day_before_yesterday_date_data["4. close"])
difference = abs(price_yesterday - price_day_before_yesterday)
difference_percent = (difference / price_yesterday) * 100

if difference_percent > 5:
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    formatted_articles = [f"Headline:{article['title']}. \nBrief: {article['description']}" for article in
                          three_articles]
    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        client_number = os.environ.get("Client")
        message = client.messages.create(
            from_="+12174724154",
            to=client_number,
            body=article
        )

        print(message.status)
