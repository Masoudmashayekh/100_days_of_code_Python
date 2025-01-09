from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://orteil.dashnet.org/experiments/cookie/"
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get(url=URL)
cookie = driver.find_element(By.ID, value="cookie")
store_items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
id_items = [item.get_attribute("id") for item in store_items]

timeout = time.time() + 5
one_min = time.time() + 60 * 1  # 1 minute

while True:
    cookie.click()
    # Every 5 seconds:
    if time.time() > timeout:
        all_prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        item_prices = []
        for price in all_prices:
            element = price.text
            if element != "":
                cost = int(element.strip().split("-")[1].replace(",", ""))
                item_prices.append(cost)

        # Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = id_items[n]

        # Get current cookie count
        money_element = driver.find_element(By.ID, value="money").text
        if "," in money_element:
            money_element.replace(",", "")
        cookie.count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id_ in cookie_upgrades.items():
            if cookie.count > cost:
                affordable_upgrades[cost] = id_
        print(affordable_upgrades)

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        x = driver.find_element(by=By.ID, value=to_purchase_id)
        print(x.text)
        x.click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    # After 1 minutes stop the bot and check the cookies per second count.
    if time.time() > one_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break

driver.quit()
