from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium .webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

#W Selenium4 jeżeli chromedriver jest w lokalizacji domyslnej to nie trzeba uzywać
#service = Service(executable_path="C:\\Users\\mjedr\\Desktop\\Selenium\\chromedriver.exe")
#driver = webdriver.Chrome(service=service)
driver = webdriver.Chrome()

#Pobiera sie webdriver https://sites.google.com/chromium.org/driver/, najlepiej wcześnie zauktalizować chrome
driver.get("https://google.com")

#To użycie find_element jest spoko, ale strony działaja asynchronicznie i moze pojawic sie blad
#cookies_button = driver.find_element(By.ID, "L2AGLb")

cookies_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "L2AGLb")))
cookies_button.click()

#input_element = driver.find_element(By.CLASS_NAME, "gLFyf")

#Czeka maksymalnie 10s aż element bedzie clickable
input_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "gLFyf")))
input_element.clear()
input_element.send_keys("larger building in the world" + Keys.ENTER)


link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "List of largest buildings")))
link.click()
time.sleep(5)

driver.quit()   