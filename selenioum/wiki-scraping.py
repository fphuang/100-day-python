from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/fp/development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('https://en.wikipedia.org/wiki/Main_Page')
article_count = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
# article_count.click()

all_portals = driver.find_element(by=By.LINK_TEXT, value="All portals")
# all_portals.click()

search = driver.find_element(by=By.NAME, value="search")
search.send_keys("python")
search.send_keys(Keys.ENTER)