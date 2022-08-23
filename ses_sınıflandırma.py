import os
from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("================ Kayıt Ediliyor ================")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("*================ Kaydedildi ================")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
from selenium.webdriver.chrome.options import Options
print("================ YAPAY ZEKAYA SESİ İNCELİYOR ================")
chrome_options = Options()

chrome_options.add_argument("--headless")

browser = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
browser.get("https://esc50.herokuapp.com")
sleep(2)
browser.find_element_by_id("inputFile").send_keys(os.getcwd()+"/output.wav")
sleep(2)
browser.find_element_by_id("uploadButton").click()
sleep(4)
print("================ TAHMİNLEME GERÇEKLEŞTİRİLİYOR ================")
sleep(4)

first_name = browser.find_element_by_xpath('//*[@id="tablediv"]/table/tbody/tr[1]/td[1]').text
browser.implicitly_wait(30)
first_trust = browser.find_element_by_xpath('//*[@id="tablediv"]/table/tbody/tr[1]/td[2]').text
browser.implicitly_wait(30)

print("================ Results ================")
print( first_trust +" Güven ile " + first_name)