from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
query="laptop"
driver = webdriver.Chrome()
driver.get(f"https://www.amazon.com/s?k={query}")

elem=driver.find_element(By.CLASS_NAME,"puis-card-container")
print(elem.get_attribute("outerHTML"))
time.sleep(6)
driver.close()