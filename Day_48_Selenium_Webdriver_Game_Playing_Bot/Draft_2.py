from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://en.wikipedia.org/wiki/Main_Page"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url=URL)

article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(article_count.text)

all_portals = driver.find_element(By.LINK_TEXT,value="Content portals")
# all_portals.click()

search = driver.find_element(By.NAME,value="search")
search.send_keys("Python", Keys.ENTER)




# driver.quit()
