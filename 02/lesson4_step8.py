# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
#
# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
import math
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    price = WebDriverWait(browser, 12).until(expected_conditions.text_to_be_present_in_element((By.ID, 'price'), '100'))
    button = browser.find_element_by_css_selector('#book')
    button.click()

    num = browser.find_element_by_css_selector('#input_value')
    browser.execute_script("return arguments[0].scrollIntoView(true);", num)
    res = calc(int(num.text))

    inp=browser.find_element_by_css_selector('#answer')
    inp.send_keys(res)

    but = browser.find_element_by_css_selector('#solve')
    but.click()



finally:
    time.sleep(5)
    browser.quit()
