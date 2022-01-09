from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class InternetSpeedTwitterBot:
    chrome_driver_path = "/Users/fp/development/chromedriver"

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        self.driver.find_element(by=By.XPATH, value="//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a").click()
        time.sleep(60)

        speed_down = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = float(speed_down)
        print(speed_down)
        speed_up = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        self.up = float(speed_up)
        print(speed_up)


    def tweet_at_provider(self):
        self.get_internet_speed()
        if self.up < 120 or self.down < 10:
            pass


my_bot = InternetSpeedTwitterBot()
my_bot.tweet_at_provider()