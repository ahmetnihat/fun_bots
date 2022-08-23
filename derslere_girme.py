from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import datetime
import time


def Join():
    browser = webdriver.Edge("msedgedriver.exe")
    browser.get("https://erciyes-edu-tr.zoom.us/j/96648741793?pwd=aFZzQ1haeG41WWFUSmkrdEhzUTZVQT09")

    time.sleep(3)
    browser.maximize_window()
    #Keys.ARROW_LEFT
    #Keys.SPACE
    pyautogui.moveTo(1130, 200, 2)
    pyautogui.click()



while True:

    ders_saati = datetime.datetime.now().time().hour
    ders_dakikası = datetime.datetime.now().time().minute
    print(f"Saat: {ders_saati,ders_dakikası}")

    if ders_saati == 18 and ders_dakikası == 43:
        print("Ders başladı")
        Join()
        break

    time.sleep(58)



