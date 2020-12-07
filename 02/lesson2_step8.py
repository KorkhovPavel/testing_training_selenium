# Напишите скрипт, который будет выполнять следующий сценарий:
#
# Открыть страницу http://suninjuly.github.io/file_input.html
# Заполнить текстовые поля: имя, фамилия, email
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# Нажать кнопку "Submit"
import os

from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('http://suninjuly.github.io/file_input.html')

    firstname = browser.find_element_by_css_selector('[name="firstname"]')
    firstname.send_keys('firstname')
    lastname = browser.find_element_by_css_selector('[name="lastname"]')
    lastname.send_keys('lastname')
    email = browser.find_element_by_css_selector('[name="email"]')
    email.send_keys('email')

    files = browser.find_element_by_css_selector('#file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'text.txt')
    files.send_keys(file_path)

    but = browser.find_element_by_css_selector('button')
    but.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()