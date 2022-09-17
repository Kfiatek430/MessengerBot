import configparser
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

config = configparser.RawConfigParser()
ConfigFilePath = r'D:\Programs\MessengerBot\config.ini'
config.read(ConfigFilePath)

user1 = config.get('MainData', 'user')
password1 = config.get('MainData', 'password')
message1 = config.get('MainData', 'message')
time1 = config.get('MainData', 'time')
receiver1 = config.get('MainData', 'receiver')

class Main:
    def GetTime():
        TimeBasic = datetime.now()
        TimeHM = TimeBasic.strftime("%H:%M")
        return TimeHM

    def SendMessage(user1, password1, message1, receiver1):
        config = Options()
        config.add_argument('disable-infobars')
        config.add_argument('--headless')

        driver = webdriver.Chrome(executable_path="d:\Programs\Drivers\chromedriver.exe", chrome_options=config)
        driver.get("https://www.messenger.com")

        accept = driver.find_element("xpath", "/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[2]")
        accept.click()

        login = driver.find_element("xpath", "/html/body/div/div/div/div[1]/div/div/div/div[1]/div/div[2]/div/div[7]/div[1]/div/div[2]/div[1]/div/form/div/input[6]")
        login.send_keys(user1)

        password = driver.find_element("xpath", "/html/body/div/div/div/div[1]/div/div/div/div[1]/div/div[2]/div/div[7]/div[1]/div/div[2]/div[1]/div/form/div/input[7]")
        password.send_keys(password1)
        password.submit()

        driver.get("https://www.messenger.com/t/100060541173100/")

        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div/div/label/input")))
        search = driver.find_element("xpath", "/html/body/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div/div/label/input")
        search.send_keys(receiver1)

        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/ul/li[1]/ul/li[2]/div/a/div/div[2]/div/div/span/span/span")))
        target_user = driver.find_element("xpath", "/html/body/div[1]/div/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/ul/li[1]/ul/li[2]/div/a/div/div[2]/div/div/span/span/span")
        target_user.click()

        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p")))
        time.sleep(2)
        input = driver.find_element("xpath", "/html/body/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p")
        input.send_keys(message1)
        time.sleep(1)
        input.send_keys(Keys.ENTER)
        time.sleep(60)

while True:
    ActualTime = Main.GetTime()
    time.sleep(5)
    print('Wait')
    if ActualTime == str(time1):
        print("Let's go")
        Main.SendMessage(user1, password1, message1, receiver1)
    else:
        pass
