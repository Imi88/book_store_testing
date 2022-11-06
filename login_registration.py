# регистрация аккаунта
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver.maximize_window()
driver.get("https://practice.automationtesting.in")
driver.find_element_by_link_text("My Account").click() # Нажали на вкладку "My Account Menu"
register = driver.find_element_by_id("reg_email")
register.send_keys("imi88@gmail.com") # В разделе "Register" ввели email для регистрации
password = driver.find_element_by_id("reg_password")
password.send_keys("Df67!_1H$?aaaasAAAAA") # В разделе "Register" ввели пароль для регистрации
strong_password = WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-password-strength.strong"),"Strong")) # без явного ожидания, кнопка Нажмите на кнопку "Register" не нажималась
driver.find_element_by_css_selector(".register .woocommerce-Button").click() # Нажали на кнопку "Register"

# логин в систему
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in")
driver.find_element_by_link_text("My Account").click() # Нажали на вкладку "My Account Menu"
username = driver.find_element_by_id("username")
username.send_keys("imi88@gmail.com") # В разделе "Login", ввели email для логина
password = driver.find_element_by_id("password")
password.send_keys("Df67!_1H$?aaaasAAAAA") # В разделе "Login", ввели пароль для логина
driver.find_element_by_css_selector(".login .woocommerce-Button").click() # Нажали на кнопку "Login"
logout = driver.find_element_by_css_selector(".woocommerce-MyAccount-navigation-link--customer-logout a")
assert logout.text == "Logout" # Проверяем, что на странице есть элемент "Logout"
