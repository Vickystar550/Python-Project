from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

PROMISE_DOWN = 70
PROMISE_UP = 20

TWITTER_EMAIL = ""
TWITTER_PASSWORD = "Vic3829kanic00049"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.down = PROMISE_DOWN
        self.up = PROMISE_UP

    def get_internet_speed(self):
        self.driver.get(url='https://www.speedtest.net/')

        # time.sleep(1)
        print('working now')

        privacy_button = self.driver.find_element_by_xpath(xpath='//*[@id="onetrust-accept-btn-handler"]')
        privacy_button.click()
        print('button clicked')
        # time.sleep(3)

        go_button = self.driver.find_element_by_css_selector(css_selector='.start-button a')
        go_button.click()

        # time.sleep(60)

    def tweet_at_provider(self):
        pass


speed_test = InternetSpeedTwitterBot()
speed_test.get_internet_speed()
