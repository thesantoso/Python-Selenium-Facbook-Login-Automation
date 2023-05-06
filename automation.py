from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.facebook.com")
driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys()
driver.find_element(By.CSS_SELECTOR, "input[name='pass']").send_keys()

button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='login']")))
button.click()

time.sleep(20)

driver.quit()
