from selenium import webdriver
import time

from webdriver_manager.chrome import ChromeDriverManager

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)

    element = browser.find_element_by_css_selector('.first_block input.first')
    element.send_keys("Мой ответ")
    time.sleep(5)
    element1 = browser.find_element_by_css_selector('.first_block input.second')
    element1.send_keys("Мой ответ")
    time.sleep(5)
    element2 = browser.find_element_by_css_selector('.first_block input.third')
    element2.send_keys("Мой ответ")
    time.sleep(5)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
