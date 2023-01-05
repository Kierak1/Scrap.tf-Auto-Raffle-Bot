from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import pickle
import pprint 
import time

def save_cookies(driver, location):

    pickle.dump(driver.get_cookies(), open(location, "wb"))

def load_cookies(driver, location, url=None):

    cookies = pickle.load(open(location, "rb"))
    driver.delete_all_cookies()
    url = "https://google.com" if url is None else url
    driver.get(url)
    for cookie in cookies:
        driver.add_cookie(cookie)

#chrome = webdriver.Chrome()
#chrome.get("https://google.com")
#time.sleep(5)
#pprint.pprint(chrome.get_cookies())
#print "--------------------------------\n"

PATH = "C:\Program Files (x86)\chromedriver"
chrome = webdriver.Chrome(PATH)
#chrome.get("https://steamcommunity.com/login")
#load_cookies(chrome, "C:\\Users\\Bigga\\Desktop\\Scripts\\Scrap.tf\\cookies3.txt")
chrome.get("https://scrap.tf")
time.sleep(35)
save_cookies(chrome, "C:\\Users\\Bigga\\Desktop\\Scripts\\Scrap.tf\\cookies2.txt")
chrome.quit()