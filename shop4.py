import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver=webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(10)

my_account=driver.find_element(By.LINK_TEXT, "My Account").click()

name_log=driver.find_element_by_id("username")
name_log.send_keys("cristinanefedova@yandex.ru")
password_log=driver.find_element_by_id("password")
password_log.send_keys("123_Cristina_456")
login_btn=driver.find_element_by_xpath("//input[@value='Login']").click()

shop_btn=driver.find_element_by_id("menu-item-40").click()

android_book=driver.find_element_by_css_selector('[href="https://practice.automationtesting.in/product/android-quick-start-guide/"]').click()

old_price=driver.find_element_by_css_selector(".price:nth-child(1)")
old_price_get_text=old_price.text
assert "₹600.00" in old_price_get_text

new_price=driver.find_element_by_xpath("//ins // span [@class='woocommerce-Price-amount amount']")
new_price_get_text=new_price.text
assert "₹450.00" in new_price_get_text

img=WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "[decoding='async']")))
img.click()

open_img=WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='pp_close']")))
open_img.click()
