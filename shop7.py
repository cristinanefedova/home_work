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

cart=driver.find_element_by_id("wpmenucartli").click()
time.sleep(5)

proceed_btn=WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")))

proceed_btn.click()

first_name=WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "billing_first_name")))

first_name=driver.find_element_by_id("billing_first_name")
first_name.send_keys("Cristina")

last_name=driver.find_element_by_id("billing_last_name")
last_name.send_keys("Nefedova")

email=driver.find_element_by_id("billing_email")
email.send_keys("cristinanefedova@yandex.ru")

phone=driver.find_element_by_id("billing_phone")
phone.send_keys("+79173136040")

country=driver.find_element_by_id("select2-chosen-1").click()
country2=driver.find_element_by_id("s2id_autogen1_search")
country2.send_keys("Russia")
russia=driver.find_element_by_class_name("select2-match").click()

address=driver.find_element_by_id("billing_address_1")
address.send_keys("Freedom")

town=driver.find_element_by_id("billing_city")
town.send_keys("Ramenskoe")

state=driver.find_element_by_id("billing_state")
state.send_keys("Moscow region")

postcode=driver.find_element_by_id("billing_postcode")
postcode.send_keys("140103")

driver.execute_script("window.scrollBy(0,600);")
time.sleep(10)

check_pay=driver.find_element_by_id("payment_method_cheque").click()

place_order=driver.find_element_by_id("place_order").click()

massage=WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"),"Thank you. Your order has been received."))

payment_check=WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot>tr:nth-child(3)"), "Check Payments"))
