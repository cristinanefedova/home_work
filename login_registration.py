import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.implicitly_wait(10)

driver.get("https://practice.automationtesting.in/")
my_account=driver.find_element(By.LINK_TEXT, "My Account").click()

email_reg=driver.find_element_by_id("reg_email")
email_reg.send_keys("cristinanefedova@yandex.ru")
password_reg=driver.find_element_by_id("reg_password")
password_reg.send_keys("123_Cristina_456")
registed_btn=driver.find_element_by_xpath("//input[@value='Register']").click()

