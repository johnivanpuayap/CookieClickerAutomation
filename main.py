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

    # Clicking the Cooking
    cookie_button = driver.find_element(By.ID, 'cookie')
    cookie_button.click()
