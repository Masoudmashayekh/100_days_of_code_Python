from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

URL = "https://shorturl.at/HnmFh"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }
response = requests.get(url=URL, headers=header)

soup = BeautifulSoup(response.content, "html.parser")
price = soup.find(class_="a-price aok-align-center reinventPricePriceToPayMargin priceToPay").get_text()
price_without_currency = price.split("€")[0].replace(",", ".")
price_as_float = float(price_without_currency)
print(price_as_float)
title = soup.find(id="productTitle").get_text().strip()
print(title)
# print(soup.prettify())

BUY_PRICE = 100
if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price_as_float}€ !"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=os.environ["my_email"], password=os.environ["password"])
        connection.sendmail(from_addr=os.environ["my_email"], to_addrs=os.environ["client"],
                            msg=f"Subject: Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8"))
