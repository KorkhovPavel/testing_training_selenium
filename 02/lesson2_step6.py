# Напишите скрипт, который будет выполнять следующий сценарий:
# Открыть страницу http://SunInJuly.github.io/execute_script.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x.
# Проскроллить страницу вниз.
# Ввести ответ в текстовое поле.
# Выбрать checkbox "I'm the robot".
# Переключить radiobutton "Robots rule!".
# Нажать на кнопку "Submit"
import math

from selenium import webdriver
import time

from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('http://SunInJuly.github.io/execute_script.html')

    element = browser.find_element_by_css_selector('#input_value')
    num = int(element.text)
    res = calc(num)

    input_res = browser.find_element_by_css_selector('#answer')
    input_res.send_keys(res)

    check = browser.find_element_by_css_selector('#robotCheckbox')
    check.click()

    button = browser.find_element_by_tag_name("#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    check = browser.find_element_by_css_selector('#robotsRule')
    check.click()

    check = browser.find_element_by_css_selector('button')
    check.click()

    # element1 = browser.find_element_by_css_selector('#num2')
    # res = int(element.text) + int(element1.text)
    # print(res)
    #
    # select = Select(browser.find_element_by_tag_name("select"))
    # select.select_by_value(str(res))
    #
    # but = browser.find_element_by_css_selector('button')
    # but.click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
