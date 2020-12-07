# Напишите код, который реализует следующий сценарий:
# Открыть страницу http://suninjuly.github.io/selects1.html  и http://suninjuly.github.io/selects2.html
# Посчитать сумму заданных чисел
# Выбрать в выпадающем списке значение равное расчитанной сумме
# Нажать кнопку "Submit"

from selenium import webdriver
import time

from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('http://suninjuly.github.io/selects2.html')

    element = browser.find_element_by_css_selector('#num1')
    element1 = browser.find_element_by_css_selector('#num2')
    res = int(element.text) + int(element1.text)
    print(res)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(res))

    but = browser.find_element_by_css_selector('button')
    but.click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
