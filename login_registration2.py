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

logout=driver.find_element(By.LINK_TEXT, "Logout")
logout_href=logout.get_attribute("href")
if logout_href=="https://practice.automationtesting.in/my-account/customer-logout/":
    print("Yes")
else:
    print("No")


