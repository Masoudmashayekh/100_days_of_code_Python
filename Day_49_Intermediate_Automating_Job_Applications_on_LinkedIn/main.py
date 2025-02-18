from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os
from dotenv import load_dotenv
import time

load_dotenv()
URL = os.environ["LINK"]
USERNAME = os.environ["USER_NAME"]
PASSWORD = os.environ["PASSWORD"]
PHONE = os.environ["PHONE"]
def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_element(by=By.XPATH, value='//*[@id="ember345"]')
    discard_button.click()

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get(url=URL)
time.sleep(2)

sign_in_b = driver.find_element(by=By.XPATH,
                                value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
sign_in_b.click()
time.sleep(2)

enter_user = driver.find_element(by=By.XPATH, value='//*[@id="base-sign-in-modal_session_key"]')
enter_user.send_keys(USERNAME)
enter_pass = driver.find_element(by=By.XPATH, value='//*[@id="base-sign-in-modal_session_password"]')
enter_pass.send_keys(PASSWORD)
enter_pass.send_keys(Keys.ENTER)
time.sleep(5)

all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")
for listing in all_listings:
    listing.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()
        time.sleep(2)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            # reject = driver.find_element(By.XPATH,value='//*[@id="ember358"]/span')
            # reject.click()
            # time.sleep(2)
            print("Complex application, skipped.")
            continue
        else:
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        # close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        # close_button.click()
        save_button = driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[2]/div/div[3]/button[2]/span")
        save_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue
