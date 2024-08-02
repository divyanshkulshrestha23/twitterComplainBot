import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PROMISED_UP = 10
PROMISED_DOWN = 300
TWITTER_EMAIL = OS.environ.get("TWITTER_EMAIL")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")
CHROME_DRIVER_PATH = "/Users/Public/Desktop/Google Chrome.lnk"
TWITTER_USERNAME = os.environ.get("TWITTER_USERNAME")


class InternetSpeedBot:
    def __init__(self, driver):
        self.google = driver
        self.up = 0
        self.down = 0

    def GetInternetSpeed(self):
        self.google.get("https://www.speedtest.net/")
        time.sleep(10)
        speedtest = self.google.find_element(By.XPATH,
                                             value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        speedtest.click()
        time.sleep(60)
        self.down = self.google.find_element(By.XPATH,
                                             value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.google.find_element(By.XPATH,
                                           value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.google.quit()

    def TweetAtProvider(self):
        self.google.get("https://twitter.com/login")
        time.sleep(10)
        #self.google.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[1]').click()
        emailInput = self.google.find_element(By.TAG_NAME, value='input')
        emailInput.send_keys(TWITTER_EMAIL, Keys.ENTER)
        time.sleep(5)
        usernameInput = self.google.find_element(By.NAME, value='text')
        usernameInput.send_keys(TWITTER_USERNAME, Keys.ENTER)
        time.sleep(5)
        passwordInput = self.google.find_element(By.NAME, value='password')
        passwordInput.send_keys(TWITTER_PASSWORD, Keys.ENTER)
        time.sleep(5)
        self.google.maximize_window()
        tweetButton = self.google.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        tweetButton.click()
        time.sleep(5)
        tweet_compose = self.google.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down} Mbps down/{self.up} Mbps up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.google.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/button[2]')
        tweet_button.click()
        time.sleep(2)
        self.google.quit()


