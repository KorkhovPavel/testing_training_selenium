# Открыть страницу http://suninjuly.github.io/get_attribute.html.
# Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
# Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
# Посчитать математическую функцию от x (сама функция остаётся неизменной).
# Ввести ответ в текстовое поле.
# Отметить checkbox "I'm the robot".
# Выбрать radiobutton "Robots rule!".
# Нажать на кнопку "Submit".

from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(' http://suninjuly.github.io/get_attribute.html')

    element = browser.find_element_by_css_selector('img')
    num = element.get_attribute("valuex")
    res = calc(num)

    input_res = browser.find_element_by_css_selector('#answer')
    input_res.send_keys(res)

    check = browser.find_element_by_css_selector('#robotCheckbox')
    check.click()

    rad = browser.find_element_by_css_selector('#robotsRule')
    rad.click()

    but = browser.find_element_by_css_selector('button')
    but.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
