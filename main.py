from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from InternetSpeedBot import InternetSpeedBot

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chromeOptions)

Bot = InternetSpeedBot(driver)
Bot.GetInternetSpeed()
Bot.TweetAtProvider()

