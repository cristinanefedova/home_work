import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(10)

driver.get("https://practice.automationtesting.in/")
my_account=driver.find_element(By.LINK_TEXT, "My Account").click()

name_log=driver.find_element_by_id("username")
name_log.send_keys("cristinanefedova@yandex.ru")
password_log=driver.find_element_by_id("password")
password_log.send_keys("123_Cristina_456")
login_btn=driver.find_element_by_xpath("//input[@value='Login']").click()

shop_btn=driver.find_element_by_id("menu-item-40").click()

element=driver.find_element_by_css_selector('[value="menu_order"]')
element_checked=element.get_attribute("selected")
if element_checked is None:
    print("No")
else:
    print("Selected")

sotr_price=driver.find_element_by_css_selector("[name='orderby']")
select=Select(sotr_price)
select.select_by_value("price-desc")

element2=driver.find_element_by_css_selector('[value="price-desc"]')
element2_checked=element2.get_attribute("selected")
if element2_checked is None:
    print("No")
else:
    print("Selected")