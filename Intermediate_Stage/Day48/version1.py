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


last_purchase_list = []     # holds purchased items for each iteration of while loop
purchase_counts = {key: 0 for key in get_store().keys()}    # holds successfully purchased items and their count

start_time = time.time()
timeout = time.time() + 5

while (time.time() - start_time) < DURATION_MIN * 60:
    button.click()

    if time.time() > timeout:
        # getting the cookies count
        click_money = int(driver.find_element_by_id(id_='money').text.strip().replace(",", ""))

        # get the store items dictionary
        store = get_store()

        # loop through the store dictionary
        for key, value in store.items():
            # check if key is already in last_purchase list
            # this helps to avoid double spending instead buy the next affordable expensive item
            if key in last_purchase_list:
                continue

            if click_money > int(value[0]):
                # purchase the most expensive one and keep track of it in last_purchase_list
                last_purchase_list.append(key)
                value[-1].click()
                # add a count for that particular upgrade level:
                purchase_counts[key] += 1
                break

        # resetting our last_purchase_list for the next iteration
        if len(last_purchase_list) == len(store):
            last_purchase_list = []

        timeout = time.time() + 5


# count per second:
cps = driver.find_element_by_id(id_='cps').text


# print(f'Your Cookie Upgrades Purchase Count: ')
# for key, value in purchase_counts.items():
#     print(f'{key}\t{value}')
print(f'Your final {cps}')


driver.quit()

