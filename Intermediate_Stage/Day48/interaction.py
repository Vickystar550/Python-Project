from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(url='https://secure-retreat-92358.herokuapp.com/')

# filling forms:
first_name = driver.find_element_by_name(name='fName')
first_name.send_keys('Victor')

last_name = driver.find_element_by_name(name='lName')
last_name.send_keys('Nice')

email = driver.find_element_by_name(name='email')
email.send_keys('victor@gmail.com')

button = driver.find_element_by_tag_name(name='button')
button.click()

driver.quit()

