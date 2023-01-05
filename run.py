from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.support.color import Color
from bs4 import BeautifulSoup
from random import randint
from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from parsel import Selector
from random import choice
import undetected_chromedriver as uc
import time
import pickle
import pprint
import re
import random
import requests
import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("ok")

def load_cookies(driver, location, url=None):
    cookies = pickle.load(open(location, "rb"))
    driver.delete_all_cookies()
    url = "https://scrap.tf/raffles/ending" if url is None else url
    driver.get(url)
    for cookie in cookies:
        driver.add_cookie(cookie)

def linksa():
    links = [link.get_attribute("href") for link in chrome.find_elements_by_xpath("//div[@class='raffle-name']/a[@href]")]
    for link in links:
         try: 
             chrome.get(link)
         except: 
             print("Links pooped")
             chrome.quit()
         try:
             WebDriverWait(chrome, 0).until(EC.element_to_be_clickable((By.XPATH,"(//button[contains(.,'Enter Raffle')])[last()]"))).click()
             print("Button found and pressed")
             sleep(randint(4,5))
         except:
             sleep(randint(0,1))
             print("Button not found but the script is still running")

def privacyskip():
    try:
        WebDriverWait(chrome, 1).until(EC.visibility_of_element_located((By.XPATH,"(//button[contains(.,'Accept')])[last()]"))).click()
    except:
        print("PrivacySkip Not Found")

def skipadsonmanncoo():
    try:
        WebDriverWait(chrome, 3).until(EC.visibility_of_element_located((By.XPATH,"(//span[contains(.,'×')])[last()]"))).click()
    except:
        print("Nigger Not Found")

def scroll():
    chrome.get("https://scrap.tf/raffles/ending")
    time.sleep(1)
    chrome.refresh()
    y = 2000
    for timer in range(0, 30):
        chrome.execute_script("window.scrollTo(0, "+str(y)+")")
        y += 4000 
        time.sleep(3)
        try:
            if (chrome.find_element_by_xpath("//div[@class='panel-body raffle-pagination-done']")).is_displayed():
                print("Loaded all raffles")
                break
        except:
            print("Not Found")

def withdraw():
         chrome.get("https://scrap.tf/raffles/ending")
         time.sleep(5)
         print("Parent window title: " + chrome.title)
         p = chrome.current_window_handle
         try:
             WebDriverWait(chrome, 2).until(EC.visibility_of_element_located((By.XPATH,"(//button[contains(.,'Withdraw Items')])[last()]"))).click()
             WebDriverWait(chrome, 50).until(EC.visibility_of_element_located((By.XPATH,"(//button[contains(.,'Open Trade Offer')])[last()]"))).click()
             time.sleep(1)
             chwnd = chrome.window_handles
             for w in chwnd:
                 if(w!=p):
                     chrome.switch_to.window(w)
                     break
             print("Child window title: " + chrome.title)
             time.sleep(1)
             b1 = chrome.find_element_by_xpath("//*[contains(text(), 'Confirm trade contents')]")
             chrome.execute_script("arguments[0].click();", b1)
             time.sleep(1)
             b2 = chrome.find_element_by_xpath("//*[contains(text(), 'Accept Trade')]")
             chrome.execute_script("arguments[0].click();", b2)
             time.sleep(10)
         except:
             print("Withdraw Failed")

def megaraffle():
    try:
        chrome.get("https://scrap.tf/megaraffle")
        privacyskip()
        WebDriverWait(chrome, 3).until(EC.element_to_be_clickable((By.XPATH,"(//div[contains(.,' Enter Megaraffle')])[last()]"))).click()
        iframe = WebDriverWait(chrome, 5).until(EC.visibility_of_element_located((By.XPATH,"(//iframe[@title='reCAPTCHA'])[last()]")))
        chrome.switch_to.frame(iframe)
        WebDriverWait(chrome, 5).until(EC.visibility_of_element_located((By.XPATH,"(//div[@class='recaptcha-checkbox-border'])[last()]"))).click()
    except:
        print("Megaraffle Failed")

def collection():
    try:
        chrome.get("https://mannco.store/giveaways")
        skipadsonmanncoo()
        links = [link.get_attribute("href") for link in chrome.find_elements_by_xpath("//div[@class='raffle-list list-group rfl']/a[@href]")]
        print("shitted1")
        for link in links:
         try: 
             chrome.get(link)
         except: 
             print("Links pooped")
             chrome.quit()
         try:
             WebDriverWait(chrome, 1).until(EC.element_to_be_clickable((By.XPATH,"(//a[contains(.,'Join Now')])[last()]"))).click()
             print("Button found and pressed")
             #sleep(randint(4,5))
         except:
             #sleep(randint(0,1))
             print("Button not found but the script is still running")
    except:
        print("shitted")

createFolder('C:\Poop\\')
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Poop")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")  
#options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('disable-infobars')
options.add_argument('--window-size=1024,768')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
chrome = webdriver.Chrome(executable_path='C:\\Program Files (x86)\\chromedriver', chrome_options=options)
chrome.minimize_window()

#load_cookies(chrome, "C:\\Users\\Bigga\\Desktop\\Scripts\\Scrap.tf\\cookies3.txt")
#load_cookies(chrome, "C:\\Users\\Bigga\\Desktop\\Scripts\\Scrap.tf\\cookies2.txt")

#collection()
#megaraffle()
#scroll()     
#linksa()
#withdraw()
time.sleep(100)
chrome.quit()