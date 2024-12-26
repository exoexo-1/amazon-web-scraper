from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
query="laptop"
driver = webdriver.Chrome()
for i in range(1,20):
    driver.get(f"https://www.amazon.com/s?k={query}&page={i}&xpid=QhFmX2APBfMiO")

    elems=driver.find_elements(By.CLASS_NAME,"puis-card-container")

    print(f"{len(elems)} items found")

    for elem in elems:
        print(elem.text)
    # # print(elem.get_attribute("outerHTML"))
        


    time.sleep(2)
driver.close()