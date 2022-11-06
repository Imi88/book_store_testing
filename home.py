# добавление комментария
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in")
driver.execute_script("window.scrollBy(0, 600);") # Скроллим страницу вниз на 600 пикселей
driver.find_element_by_css_selector(".col3-1:nth-child(1) h3").click() # Нажимаем на название книги "Selenium Ruby"
driver.execute_script("window.scrollBy(0, 700);")
driver.find_element_by_class_name("reviews_tab").click() # Нажимаем на вкладку "REVIEWS"
driver.find_element_by_css_selector(".stars a:nth-child(5)").click() # Ставим 5 звёзд
field_review = driver.find_element_by_id("comment")
field_review.send_keys("Nice book!") # Заполнили поле "Review" сообщением: "Nice book!"
driver.execute_script("window.scrollBy(0, 600);")
field_name = driver.find_element_by_id("author")
field_name.send_keys("Irina") # Заполнили поле "Name"
field_email = driver.find_element_by_id("email")
field_email.send_keys("example@mail.ru") # Заполнили поле "Email"
driver.find_element_by_css_selector(".form-submit .submit").click() # Нажали на кнопку "SUBMIT"
