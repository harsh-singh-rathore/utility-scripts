import numpy as np
import time
from selenium import webdriver

# adding options for headless scraping(no browser popup)
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

driver = webdriver.Chrome()
time.sleep(3)
driver.quit()
