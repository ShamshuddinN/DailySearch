from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains



words = input('Enter Words sp sep  ').split(',')
swords = []

for i in words:
    swords.append(i.strip())



options = webdriver.EdgeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Edge(options=options)

driver.get('https://www.bing.com/')
driver.implicitly_wait(1)
time.sleep(2)
inputBox = driver.find_element(by=By.XPATH, value='//*[@id="sb_form_q"]')
inputBox.send_keys('Countries in the world')


time.sleep(2)
ActionChains(driver)\
    .key_down(Keys.ENTER)\
    .key_up(Keys.ENTER)\
    .perform()
time.sleep(2)


# //*[@id="sb_form_q"]
# insideInput.send_keys('Hello Mars')
print('Search List: ' ,swords)
for i in swords:
    time.sleep(2)
    insideInput = driver.find_element(by=By.XPATH, value='//*[@id="sb_form_q"]')
    insideInput.clear()
    insideInput.send_keys(i)
    time.sleep(1)
    ActionChains(driver)\
        .key_down(Keys.ENTER)\
        .key_up(Keys.ENTER)\
        .perform()
    time.sleep(3)

driver.close()



# dsenv\scripts\activate
# py autoSearch.py