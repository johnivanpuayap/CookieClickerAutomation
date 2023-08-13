import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Using Selenium with webdriver_manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://orteil.dashnet.org/experiments/cookie/')

start_time = time.time()
end_time = start_time + (5 * 60)
last_action_time = start_time

while time.time() < end_time:
    current_time = time.time()

    # Check What To Buy
    if current_time - last_action_time >= 5:
        money = int(driver.find_element(By.ID, 'money').text)
        store = driver.find_element(By.ID, 'store')
        products = store.find_elements(By.TAG_NAME, 'div')

        # Using a reverse loop to start checking from the most expensive product
        for product in products[::-1]:
            try:
                click_this = product.find_element(By.TAG_NAME, 'b')
                elements = click_this.text
                amount = int(elements.split(' - ')[1].replace(',', ''))
                while money > amount:
                    product.click()
                    money -= amount
            except NoSuchElementException:
                print(f"Didn't find the element")
                continue
            except IndexError:
                continue
        last_action_time = current_time

    # Clicking the Cooking
    cookie_button = driver.find_element(By.ID, 'cookie')
    cookie_button.click()
