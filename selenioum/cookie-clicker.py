from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import locale
import time

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


def get_price(selector):
    price_text = driver.find_element(by=By.CSS_SELECTOR, value=selector).text
    print(price_text)
    return locale.atof(price_text.split(" ")[-1])


chrome_driver_path = "/Users/fp/development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie_button = driver.find_element(by=By.CSS_SELECTOR, value="div#cookie")

selectors = ["div#store div#buyCursor", "div#store div#buyGrandma",
             "div#store div#buyFactory", "div#store div#buyMine",
             "div#store div#buyShipment", "div#store div#buyAlchemy\ lab",
             "div#store div#buyPortal", "div#store div#buyTime\ machine"]

price_list = [get_price(f"{selector} b") for selector in selectors]

current_time = time.time()
while True:
    cookie_button.click()
    if time.time() - current_time >= 10:
        selector = ""
        current_money = get_price("div#game div#money")
        for n in range(len(price_list)):
            if price_list[n] <= current_money:
                selector = selectors[n]

        if selector != "":
            buy_element = driver.find_element(by=By.CSS_SELECTOR, value=selector)
            buy_element.click()
        current_time = time.time()

driver.quit()