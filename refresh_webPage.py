import time
from selenium import webdriver
#from selenium.common.keys import Keys

#driver = webdriver.Firefox()
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://github.com/sheikhshakibhossain')

while True:
    time.sleep(1)
    driver.refresh()

driver.quit()
