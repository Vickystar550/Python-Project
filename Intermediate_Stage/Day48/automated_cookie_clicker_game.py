from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# set game duration
DURATION_MIN = 2

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(url='https://orteil.dashnet.org/experiments/cookie/')

# cookie button and clicking
button = driver.find_element_by_id(id_='cookie')


def get_store():
    """get the list of available upgrade levels"""
    stores = driver.find_elements_by_css_selector(css_selector='div#store div b')

    store_dict = {}
    for i in range(len(stores)):
        name = stores[i].text.split('-')[0].strip()
        amount = stores[i].text.split('-')[-1].strip().replace(",", "")

        # checking for empty strings
        if name != '' or amount != '':
            # store name as the key, amount and the instance of each corresponding item as the value...
            store_dict.update({
                name: [amount, stores[i]]
            })
    return store_dict


timeout = time.time() + 5

start_time = time.time()
while (time.time() - start_time) < DURATION_MIN * 60:
    button.click()

    if time.time() > timeout:
        # getting the cookies count
        click_money = int(driver.find_element_by_id(id_='money').text.strip().replace(",", ""))

        # get the store items dictionary
        store = get_store()

        affordable_dict = {key: int(value[0]) for (key, value) in store.items() if click_money > int(value[0])}

        for k, v in affordable_dict.items():
            if v == max(affordable_dict.values()):
                # make purchase:
                store.get(k)[-1].click()

        timeout = time.time() + 5

# count per second:
cps = driver.find_element_by_id(id_='cps').text
print(f'Your final {cps}')


driver.quit()

