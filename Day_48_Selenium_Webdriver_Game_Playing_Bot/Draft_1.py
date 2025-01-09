from selenium import webdriver
from selenium.webdriver.common.by import By
URL = "https://shorturl.at/nAxd1"
URL_2 = "https://www.python.org/"
# Keep Chrome browser open after program finishes:
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url=URL_2)

# price_euro = driver.find_element(By.CLASS_NAME,value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME,value="a-price-fraction")
# print(f"The price is {price_euro.text}.{price_cents.text}")

# search_bar = driver.find_element(By.NAME,value="q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))
#
# button = driver.find_element(By.ID,value="submit")
# print(button.size)
#
# documentation_link = driver.find_element(By.CSS_SELECTOR,value=".documentation-widget a")
# print(documentation_link.text)
#
# bug_link = driver.find_element(By.XPATH,value= '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

events = {}
event_times = driver.find_elements(By.CSS_SELECTOR,value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR,value= ".event-widget li a")
for n in range(len(event_times)):
    events[n] ={
        "time": event_times[n].text,
        "name": event_names[n].text
    }

print(events)


# driver.close()
driver.quit()
