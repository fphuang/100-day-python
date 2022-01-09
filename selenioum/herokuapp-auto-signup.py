from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/fp/development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('http://secure-retreat-92358.herokuapp.com/')

first_name = driver.find_element(by=By.NAME, value="fName")
first_name.send_keys("Fangping")
last_name = driver.find_element(by=By.NAME, value="lName")
last_name.send_keys("Huang")
email = driver.find_element(by=By.NAME, value="email")
email.send_keys("huang.fp@gmail.com")
sign_up_button = driver.find_element(by=By.CSS_SELECTOR, value="form button")
sign_up_button.click()