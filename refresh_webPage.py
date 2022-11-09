import time
from selenium import webdriver

# select path of chrome driver
driver = webdriver.Chrome('/usr/local/bin/chromedriver') 
driver.get('https://github.com/sheikhshakibhossain') # url

# refresh the page after 1 second
while True:
    time.sleep(1)
    driver.refresh()

driver.quit()
