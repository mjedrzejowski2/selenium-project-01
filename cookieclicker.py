from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium .webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time



driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")

wait = WebDriverWait(driver, 10)

cookies_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "fc-button-label")))
cookies_button.click()

#Mozna to zrobić przez XPATH
# //* - Znajduje wszystkie elementy w dokumencie, niezależnie od ich tagu (np. <div>, <span>, <button> itp.)
# [contains(text(), 'Polski')], 
# To jest filtr, który wybiera tylko te elementy, które zawierają tekst "Polski". Użycie contains oznacza, że nie musi to być dokładne dopasowanie; wystarczy, że element zawiera ten tekst.
language_button = wait.until(
 EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Polski')]")))
#language_button = wait.until(EC.element_to_be_clickable((By.ID, "langSelect-PL")))
language_button.click()

cookie_id = "bigCookie"
cookies_number = "cookies"
product_prefix = "productPrice"

time.sleep(2)

cookie = wait.until(EC.element_to_be_clickable((By.ID, cookie_id)))
cookie.click()

while True:
    cookie.click()
    cookies_count = driver.find_element(By.ID, cookies_number).text.split(" ")[0]
    cookies_count = int(cookies_count.replace(",", ""))


    for i in range(4):
        product_price = driver.find_element(By.ID, product_prefix + str(i)).text.replace(",", "")

        if not product_price.isdigit():
            continue

        product_price = int(product_price)

        if cookies_count >= product_price:
            product = wait.until(EC.element_to_be_clickable((By.ID, "product" + str(i)))) 
            product.click()
            break