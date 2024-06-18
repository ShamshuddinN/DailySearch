from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from pynput.keyboard import Key, Controller
from selenium.webdriver import Keys


words = input('Enter Words sp sep  ').split(',')
swords = []

for i in words:
    swords.append(i.strip())



driver = webdriver.Edge()
options = webdriver.EdgeOptions()
options.add_argument("--start-maximized")
options.binary_location = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'
driver = webdriver.Edge(options=options)
driver.get('https://www.bing.com/')
driver.implicitly_wait(30)
keyboard = Controller()
time.sleep(2)
inputBox = driver.find_element(by=By.XPATH, value='//*[@id="sb_form_q"]')
inputBox.send_keys('Countries in the world')
time.sleep(2)
keyboard.press(Key.enter)
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
    insideInput.send_keys(Keys.ENTER)
    time.sleep(3)

driver.close()


# py autoSearch.py