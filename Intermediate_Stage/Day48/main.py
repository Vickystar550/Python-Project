from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import json

# # keep chrome opens after program finishes
# chrome_option = webdriver.ChromeOptions()
# chrome_option.add_experimental_option("detach", True)


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(url='https://www.python.org/events/')

# scraping to get Python Upcoming Events:
event_title = driver.find_elements(By.CLASS_NAME, 'event-title')
event_location = driver.find_elements(By.CSS_SELECTOR, 'span.event-location')
event_time = driver.find_elements(By.TAG_NAME, 'time')

events = {}

for i in range(len(event_title)):
    events.update({
        i+1: {
            'name': event_title[i].text,
            'time': event_time[i].get_attribute('datetime').split('T')[0],
            'location': event_location[i].text,
        }
    })

print(events)

# saving our upcoming events to a json file
with open('upcoming_python_events.json', 'w') as file:
    json.dump(events, file, indent=4)

driver.quit()
