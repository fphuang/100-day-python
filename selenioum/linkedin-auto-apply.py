from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "/Users/fp/development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
sign_in_button = driver.find_element(by=By.CSS_SELECTOR, value="div.nav__cta-container a.nav__button-secondary")
sign_in_address = sign_in_button.get_attribute('href')


def log_in(address):
    driver.get(address)
    input_user_name = driver.find_element(by=By.CSS_SELECTOR, value="input#username")
    input_user_password = driver.find_element(by=By.CSS_SELECTOR, value="input#password")
    sign_in = driver.find_element(by=By.XPATH, value="//*[@id='organic-div']/form/div[3]/button")
    input_user_name.send_keys("huang.fp@gmail.com")
    input_user_password.send_keys("@Caseolin406linkedin")
    sign_in.click()


driver.get(sign_in_address)
log_in(sign_in_address)
time.sleep(2)

easy_apply_button = driver.find_element(by=By.XPATH, value="//*[@id='ember431']")
easy_apply_button.click()

next_button = driver.find_element(by=By.XPATH, value="//*[@id='ember447']")
next_button.click()
time.sleep(1)
next_button.click()
authorization_yes = driver.find_element(by=By.XPATH, value="//*[@id='ember437']/div/form/div/div/div[1]/fieldset/div/div[1]/label/span")
authorization_yes.click()
comfy_commute_yes = driver.find_element(by=By.XPATH, value="//*[@id='ember437']/div/form/div/div/div[2]/fieldset/div/div[1]/label/span")
comfy_commute_yes.click()
review_button = driver.find_element(by=By.CSS_SELECTOR, value=".artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view")
review_button.click()
time.sleep(5)

driver.back()



# driver.quit()