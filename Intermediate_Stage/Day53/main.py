from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time


FORM_LINK = 'https://forms.gle/gzTtmTWH6F5kKnyi6'

URL = 'https://appbrewery.github.io/Zillow-Clone/'


r = requests.get(url=URL)

soup = BeautifulSoup(r.text, 'html.parser')

listing_links = [h.get('href') for h in soup.select(selector='.property-card-link')]

prices_list = [price.getText().split('+')[0].replace('/mo', '').strip() for price in soup.select(selector='div.PropertyCardWrapper') if '$' in price.text]

addresses_list = [a.getText().strip().replace('|', '').replace("  ", '') for a in soup.find_all(name='address')]


# Filling the form using Selenium:

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

for n in range(len(listing_links)):
    driver.get(url=FORM_LINK)
    # time.sleep(1)

    address = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')

    price = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')

    link = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address.send_keys(addresses_list[n])
    price.send_keys(prices_list[n])
    link.send_keys(listing_links[n])
    submit_button.click()

driver.quit()
