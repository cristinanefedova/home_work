import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver=webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(10)

shop_btn=driver.find_element_by_id("menu-item-40").click()

add_to_basket=driver.find_element_by_css_selector("[data-product_id='182']").click()

time.sleep(10)

test=driver.find_element_by_css_selector('[class="cartcontents"]')
test_text=test.text
assert "1 Item" in test_text


test2=driver.find_element_by_css_selector(".wpmenucart-contents .amount")
test2_text=test2.text
assert "₹180.00" in test2_text

cart=driver.find_element_by_id("wpmenucartli").click()


subtotal=WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-subtotal .woocommerce-Price-amount")))
subtotal_text=subtotal.text
assert "180.00" in subtotal.text


total=WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount")))
total_text=total.text
assert "183.60" in total_text



























