# Сценарий для реализации выглядит так:
#
# Открыть страницу http://suninjuly.github.io/redirect_accept.html
# Нажать на кнопку
# Переключиться на новую вкладку
# Пройти капчу для робота и получить число-ответ
import math

from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('http://suninjuly.github.io/redirect_accept.html')

    button = browser.find_element_by_css_selector('button')
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    num = browser.find_element_by_css_selector('#input_value')
    res = calc(int(num.text))
    print(res)

    inp_num = browser.find_element_by_css_selector('#answer')
    inp_num.send_keys(res)

    enter = browser.find_element_by_css_selector('button')
    enter.click()

finally:
    time.sleep(10)
    browser.quit()
