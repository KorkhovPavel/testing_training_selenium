# Тест успешно проходит на странице http://suninjuly.github.io/registration1.html
# Тест падает с ошибкой NoSuchElementException http://suninjuly.github.io/registration2.html
# Используемые селекторы должны быть уникальны

# функция запускает две ссылки по очереди первая = "http://suninjuly.github.io/registration1.html",
# вторая = "http://suninjuly.github.io/registration2.html"
# на второй ссылке останавливается т.к поле 'Last name*' отсутвует ошибка: selenium.common.exceptions.
# NoSuchElementException: Message: no such element: Unable to locate element: {"method":"css selector",
# "selector":".first_block input.second"}

from selenium import webdriver
import time

from webdriver_manager.chrome import ChromeDriverManager


def func(link):
    try:
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get(link)

        element = browser.find_element_by_css_selector('.first_block input.first')
        element.send_keys("Мой ответ")
        time.sleep(2)
        element1 = browser.find_element_by_css_selector('.first_block input.second')
        element1.send_keys("Мой ответ")
        time.sleep(2)
        element2 = browser.find_element_by_css_selector('.first_block input.third')
        element2.send_keys("Мой ответ")
        time.sleep(2)

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(5)

        welcome_text_elt = browser.find_element_by_tag_name("h1")

        welcome_text = welcome_text_elt.text

        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()


links = ["http://suninjuly.github.io/registration1.html", "http://suninjuly.github.io/registration2.html"]
for i in links:
    func(link=i)
