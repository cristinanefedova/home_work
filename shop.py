import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
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
book=driver.find_element_by_xpath("// li[@class='post-181 product type-product status-publish product_cat-html product_tag-html has-post-title no-post-date has-post-category has-post-tag has-post-comment has-post-author  instock taxable shipping-taxable purchasable product-type-simple']").click()

title=driver.find_element_by_xpath("// h1[@itemprop='name']")
title_get_text=title.text
assert "HTML5 Forms"  in title_get_text

