from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Edge("msedgedriver.exe")

browser.get("https://10fastfingers.com/widgets/typingtest")
time.sleep(5)

i = 0
while i < 200:
    i = i + 1
    kelime = browser.find_element_by_xpath(f'//*[@id="row1"]/span[{i}]').text
    browser.find_element_by_xpath('//*[@id="inputfield"]').send_keys(kelime)
    browser.find_element_by_xpath('//*[@id="inputfield"]').send_keys(Keys.SPACE)


