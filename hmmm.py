import tweepy
from dotenv import load_dotenv
load_dotenv()

hrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

driver = webdriver.Chrome()
time.sleep(3)
driver.quit()