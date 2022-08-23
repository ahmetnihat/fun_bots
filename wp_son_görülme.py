from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime


browser = webdriver.Edge("msedgedriver.exe")

browser.get("https://web.whatsapp.com/")
time.sleep(10)

loginClick = browser.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/span/span')

loginClick.click()


data = browser.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/header/div[2]/div[2]').click()
time.sleep(3)
data2 = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[1]/div[2]/span[2]/div/span').text
print(data2)
print(time)

while True:
    data3 = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[1]/div[2]/span[2]/div/span').text
    if data2 != data3:
        if data2 != "yazıyor...":
            an = datetime.datetime.now()
            print(an , data3)
            data2 = data3
    time.sleep(1)