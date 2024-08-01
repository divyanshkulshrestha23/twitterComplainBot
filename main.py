from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from InternetSpeedBot import InternetSpeedBot

PROMISED_UP = 10
PROMISED_DOWN = 150
TWITTER_EMAIL = "divyanshkul18@gmail.com"
TWITTER_PASSWORD = "Divkul#23259"
CHROME_DRIVER_PATH = "/Users/Public/Desktop/Google Chrome.lnk"

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chromeOptions)

Bot = InternetSpeedBot(driver)
Bot.GetInternetSpeed()
Bot.TweetAtProvider()

