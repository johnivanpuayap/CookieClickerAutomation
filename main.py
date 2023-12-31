import time
from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Using Selenium with webdriver_manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://orteil.dashnet.org/experiments/cookie/')


def buy_products():
    # My Solution
    # money = int(driver.find_element(By.ID, 'money').text)
    # store = driver.find_element(By.ID, 'store')
    # products = store.find_elements(By.TAG_NAME, 'div')
    # Using a reverse loop to start checking from the most expensive product
    # for product in products[::-1]:
    #     try:
    #         click_this = product.find_element(By.TAG_NAME, 'b')
    #         elements = click_this.text
    #         amount = int(elements.split(' - ')[1].replace(',', ''))
    #         while money >= amount:
    #             product.click()
    #             money -= amount
    #     except NoSuchElementException:
    #         continue
    #     except IndexError:
    #         continue
    #     except StaleElementReferenceException:
    #         continue

    # Interesting solution I saw on the internet
    products = driver.find_elements(By.CSS_SELECTOR, "#store > div:not(.grayed)")
    products[-1].click()


start_time = time.time()
end_time = start_time + (5 * 60)
last_action_time = start_time

while time.time() < end_time:
    current_time = time.time()

    # Check What To Buy
    if current_time - last_action_time >= 10:
        buy_products()
        last_action_time = current_time

    # Clicking the Cookie
    cookie_button = driver.find_element(By.ID, 'cookie')
    cookie_button.click()

cookies_per_second = driver.find_element(By.ID, 'cps')
print("Finished 5 minutes of automation! Here is the result: ")
print(f"Cookies per second: {cookies_per_second.text}")
