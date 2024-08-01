import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver=webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(10)

shop_btn=driver.find_element_by_id("menu-item-40").click()
time.sleep(5)

driver.execute_script("window.scrollBy(0,300);")
time.sleep(3)

add_to_basket1=driver.find_element_by_css_selector("[data-product_id='182']").click()
time.sleep(5)

add_to_basket2=driver.find_element_by_css_selector("[data-product_id='180']").click()
time.sleep(5)

cart=driver.find_element_by_id("wpmenucartli").click()
time.sleep(5)
delete_book1=driver.find_element_by_css_selector("[data-product_id='182']").click()
time .sleep(5)

undo=driver.find_element_by_css_selector(".woocommerce-message>a").click()

locator=driver.find_element_by_tag_name("[name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']").clear()
time.sleep(10)

quantity_book=driver.find_element_by_tag_name("[name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']")
quantity_book.send_keys(3)
time.sleep(10)

update_basket=driver.find_element_by_css_selector("[value='Update Basket']").click()
time.sleep(10)

quantity=driver.find_element_by_tag_name("[name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']")
quantity_check=quantity.get_attribute("value")
if quantity_check ==3:
    print("3")
else:
    print("No")

time.sleep(10)

apply_coupon=driver.find_element_by_css_selector('[value="Apply Coupon"]').click()

massage=driver.find_element(By.CSS_SELECTOR,".woocommerce-error>li")
massage_text=massage.text
assert "Please enter a coupon code." in massage_text

