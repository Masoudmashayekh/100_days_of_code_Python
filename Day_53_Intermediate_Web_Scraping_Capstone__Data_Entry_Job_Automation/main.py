import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()

URL = os.environ["URL"]
GOOGLE_FORM_URL = os.environ["GOOGLE_FORM_URL"]

response = requests.get(url=URL)
web_response = response.text
soup = BeautifulSoup(web_response, "html.parser")
prices = soup.select(".PropertyCardWrapper span")
price_list = [x.getText().replace("/mo", "").split("+")[0] for x in prices]

links = soup.select(".StyledPropertyCardDataWrapper a")
links_list = [link["href"] for link in links]

address = soup.select(".StyledPropertyCardDataWrapper address")
address_list = [add.getText().replace(" | ", " ").strip() for add in address]

print(address_list)
print(price_list)
print(links_list)

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_option)

for n in range(len(links_list)):
    driver.get(url=GOOGLE_FORM_URL)
    time.sleep(3)

    input_address = driver.find_element(By.XPATH,
                                        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input_price = driver.find_element(By.XPATH,
                                      value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input_link = driver.find_element(By.XPATH,
                                     value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    input_address.send_keys(address_list[n])
    input_price.send_keys(price_list[n])
    input_link.send_keys(links_list[n])
    submit.click()
    time.sleep(2)

driver.quit()
