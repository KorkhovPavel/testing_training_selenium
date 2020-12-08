# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

# Открыть страницу http://suninjuly.github.io/alert_accept.html
# Нажать на кнопку
# Принять confirm
# На новой странице решить капчу для роботов, чтобы получить число с ответом
import math

from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('http://suninjuly.github.io/alert_accept.html')

    but = browser.find_element_by_css_selector('button')
    but.click()

    alert = browser.switch_to.alert
    alert.accept()

    num = browser.find_element_by_css_selector('#input_value')
    res = int(num.text)
    res = calc(res)

    inp_num = browser.find_element_by_css_selector('#answer')
    inp_num.send_keys(res)

    enter = browser.find_element_by_css_selector('button')
    enter.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
