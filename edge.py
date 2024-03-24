from selenium import webdriver
import time

options = webdriver.EdgeOptions()
options.binary_location = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'
driver = webdriver.Edge(options=options)

driver.get('https://www.bing.com/')

time.sleep(10)

driver.close()
