import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(10)

driver.get("https://practice.automationtesting.in/")
my_account=driver.find_element(By.LINK_TEXT, "My Account").click()

name_log=driver.find_element_by_id("username")
name_log.send_keys("cristinanefedova@yandex.ru")
password_log=driver.find_element_by_id("password")
password_log.send_keys("123_Cristina_456")
login_btn=driver.find_element_by_xpath("//input[@value='Login']").click()


shop_btn=driver.find_element_by_id("menu-item-40").click()
html=driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/product-category/html/']").click()

items_html3=driver.find_elements_by_class_name("woocommerce-LoopProduct-link")
if len(items_html3)==3:
    print("Отображаются 3 товара")
else:
    print("error")
