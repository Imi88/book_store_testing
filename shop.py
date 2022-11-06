# отображение страницы товара
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in")
driver.find_element_by_link_text("My Account").click()
username = driver.find_element_by_id("username")
username.send_keys("imi88@gmail.com")
password = driver.find_element_by_id("password")
password.send_keys("Df67!_1H$?aaaasAAAAA")
driver.find_element_by_css_selector(".login .woocommerce-Button").click() #логин
driver.find_element_by_css_selector(".menu-item:nth-child(1) a").click() #вкладка shop
driver.execute_script("window.scrollBy(0, 600);")
driver.find_element_by_css_selector(".masonry-done :nth-child(3)  .woocommerce-LoopProduct-link").click() #Открываем книгу "HTML 5 Forms"
header = driver.find_element_by_tag_name("h1")
text_header = header.text
print("Заголовок книги называется:",text_header)


# количество товаров в категории
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in")
driver.find_element_by_link_text("My Account").click()
username = driver.find_element_by_id("username")
username.send_keys("imi88@gmail.com")
password = driver.find_element_by_id("password")
password.send_keys("Df67!_1H$?aaaasAAAAA")
driver.find_element_by_css_selector(".login .woocommerce-Button").click() #логин
driver.find_element_by_css_selector(".menu-item:nth-child(1) a").click() #вкладка shop
driver.find_element_by_css_selector(".cat-item-19 a").click() #открываем категорию "HTML"
items_count = driver.find_element_by_css_selector(".current-cat span")
if items_count.text == "(3)":
    print("Отображается три товара")
else:
    print("Отображается",items_count.text,"товара") #проверка количества отоброжаемых товаров

#сортировка товаров
import time
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.support.select import Select
driver.maximize_window()
driver.get("https://practice.automationtesting.in")
driver.find_element_by_link_text("My Account").click()
username = driver.find_element_by_id("username")
username.send_keys("imi88@gmail.com")
password = driver.find_element_by_id("password")
password.send_keys("Df67!_1H$?aaaasAAAAA")
driver.find_element_by_css_selector(".login .woocommerce-Button").click() #логин
driver.find_element_by_css_selector(".menu-item:nth-child(1) a").click() #вкладка shop
default_sort = driver.find_element_by_css_selector(".orderby option:nth-child(1)")
if default_sort.get_attribute("value") == "menu_order":
    print("В селекторе выбран вариант сортировки по умолчанию")
else:
    print("Ошибка! В селекторе НЕ выбран вариант сортировки по умолчанию") #проверка сортировки по умолчанию
element = driver.find_element_by_class_name("orderby")
select = Select(element)
select.select_by_value("price-desc") #сортировка цены от большей к меньшей с помощью класса Select
time.sleep(3)
select_sort = driver.find_element_by_css_selector(".orderby option:nth-child(6)")
if select_sort.get_attribute("value") == "price-desc":
    print("В селекторе выбран вариант сортировки по цене от большей к меньшей")
else:
    print("Ошибка! В селекторе НЕ выбран вариант сортировки по цене от большей к меньшей") #проверка сортировки по умолчанию

#отображение, скидка товара
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver.maximize_window()
driver.get("https://practice.automationtesting.in")
driver.find_element_by_link_text("My Account").click()
username = driver.find_element_by_id("username")
username.send_keys("imi88@gmail.com")
password = driver.find_element_by_id("password")
password.send_keys("Df67!_1H$?aaaasAAAAA")
driver.find_element_by_css_selector(".login .woocommerce-Button").click() #логин
driver.find_element_by_css_selector(".menu-item:nth-child(1) a").click() #вкладка shop
driver.execute_script("window.scrollBy(0, 600);")
driver.find_element_by_css_selector(".masonry-done li:nth-child(1)").click() #открываем книгу "Android Quick Start Guide"
old_price = driver.find_element_by_css_selector("del>span")
assert old_price.text == "₹600.00"
print("Содержимое старой цены = '₹600.00'") #роверка старой цены
new_price = driver.find_element_by_css_selector(".entry-summary ins")
assert new_price.text == "₹450.00"
print("Содержимое старой цены = '₹450.00'") #проверка новой цены
img = WebDriverWait(driver, 10).until_not(
    EC. invisibility_of_element_located((By.CSS_SELECTOR, ".images img"))) #проверяем, что картинка есть на странице
driver.find_element_by_css_selector(".images img").click()
save_changes_btn = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")) ) #проверяем, что крестик кликабелен
driver.find_element_by_class_name("pp_close").click() # Закрыли предпросмотр, нажав на крестик

# проверка цены в корзине
import time
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver.maximize_window()
driver.get("https://practice.automationtesting.in")
driver.find_element_by_css_selector(".menu-item:nth-child(1) a").click() #вкладка shop
driver.execute_script("window.scrollBy(0, 600);")
driver.find_element_by_css_selector(".products.masonry-done li:nth-child(4) .add_to_cart_button").click() # добавили в корзину книгу "HTML5 WebApp Development"
time.sleep(5)
amount = driver.find_element_by_class_name("cartcontents")
price = driver.find_element_by_css_selector(".wpmenucart-contents .amount")
print(amount.text)
assert amount.text == "1 Item"
assert price.text == "₹180.00"
print("Количество товаров в корзине = '1 Item', а стоимость = '₹180.00'")
driver.find_element_by_class_name("wpmenucart-icon-shopping-cart-0").click() # Перешли в корзину
subtotal_check = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart_totals .cart-subtotal .woocommerce-Price-amount"),"180.00"))
subtotal = driver.find_element_by_css_selector(".cart_totals .cart-subtotal .woocommerce-Price-amount")
assert subtotal.text == "₹180.00" # проверяем, что в Subtotal отобразилась стоимость
total_check = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .amount"),"₹183.60"))
total = driver.find_element_by_css_selector(".order-total .amount")
assert total.text == "₹183.60" # проверяем, что в Total отобразилась стоимость

# работа в корзине
import time
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.support.select import Select
driver.maximize_window()
driver.get("https://practice.automationtesting.in")
driver.find_element_by_css_selector(".menu-item:nth-child(1) a").click() #вкладка shop
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element_by_css_selector(".products.masonry-done li:nth-child(4) .add_to_cart_button").click() # добавили в корзину книгу "HTML5 WebApp Development"
time.sleep(3)
driver.find_element_by_css_selector(".products.masonry-done li:nth-child(5) .add_to_cart_button").click() # добавили в корзину книгу "JS Data Structures and Algorithm"
driver.find_element_by_class_name("wpmenucart-icon-shopping-cart-0").click() # перешли в корзину
time.sleep(3)
driver.find_element_by_css_selector(".shop_table .cart_item:nth-child(1) .remove").click() # Удалили первую книгу
time.sleep(3)
driver.find_element_by_css_selector(".woocommerce-message a").click() # нажали на Undo (отмена удаления)
quantity = driver.find_element_by_css_selector(".cart_item:nth-child(1) input")
quantity.clear() # очистили поле Quantity
quantity.send_keys("3") # увеличили количесто товара до 3 шт для "JS Data Structures and Algorithm“
driver.find_element_by_css_selector(".coupon .button").click()
num_quantity = quantity.get_attribute("value")
assert int(num_quantity) == 3 # тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3
print ("value элемента quantity для 'JS Data Structures and Algorithm' равно 3")
time.sleep(3)
driver.find_element_by_css_selector(".coupon .button").click() # Нажали на кнопку "APPLY COUPON"
message = driver.find_element_by_css_selector(".woocommerce-error li")
assert message.text == "Please enter a coupon code."
print ("Возникло сообщение: 'Please enter a coupon code.'")

# покупка товара
import time
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver.maximize_window()
driver.get("https://practice.automationtesting.in")
driver.find_element_by_css_selector(".menu-item:nth-child(1) a").click() #вкладка shop
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element_by_css_selector(".products.masonry-done li:nth-child(4) .add_to_cart_button").click() # добавили в корзину книгу "HTML5 WebApp Development"
time.sleep(3)
driver.find_element_by_class_name("wpmenucart-icon-shopping-cart-0").click() # перешли в корзину
wait = WebDriverWait(driver, 20)
checkout_btn = wait.until(
    EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")) )
driver.find_element_by_class_name("checkout-button").click() # Нажали "PROCEED TO CHECKOUT"
check_name = wait.until_not(
    EC.invisibility_of_element_located((By.XPATH, "//p[@id='billing_first_name_field']/label"))) # явное ожидание для first name
first_name = driver.find_element_by_id("billing_first_name")
first_name.send_keys("Irina") # заполнили first name
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Smirnova") # заполнили last name
email = driver.find_element_by_id("billing_email")
email.send_keys("example@mail.ru") # заполнили email
tel = driver.find_element_by_id("billing_phone")
tel.send_keys("89117883289") # заполнили tel
driver.find_element_by_id("select2-chosen-1").click()
driver.find_element_by_css_selector(".page .select2-drop-active .select2-input").click()
driver.find_element_by_css_selector(".select2-result:nth-child(111)").click() #выбор селектора country
town = driver.find_element_by_xpath("//input[@name='billing_city']")
town.send_keys("Kingston") # заполнили town
address = driver.find_element_by_xpath("//input[@name='billing_address_1']")
address.send_keys("New-Kingston 1st street 23 flat 13") # заполнили address
state = driver.find_element_by_xpath("//input[@name='billing_state']")
state.send_keys("New-Kingston") # заполнили state
postcode = driver.find_element_by_xpath("//input[@name='billing_postcode']")
postcode.send_keys("JMAAW04") # заполнили Postcode
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
driver.find_element_by_id("payment_method_cheque").click() # выбрали способ оплаты "Check Payments"
driver.find_element_by_id("place_order").click() # нажали PLACE ORDER
thanks = wait.until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received.")) # явное ожидание, что отображается надпись "Thank you. Your order has been received."
payment = wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr:nth-child(3)"), "Check Payments")) # явное ожидание, что в Payment Method отображается текст "Check Payments"



