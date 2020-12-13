# Инопланетяне оставляют загадочные сообщения на Stepik в фидбеке задач на правильное решение. Мы смогли локализовать
# несколько url-адресов задач, где появляются кусочки сообщений. Ваша задача — реализовать автотест со следующим
# сценарием действий:
#
# открыть страницу
# ввести правильный ответ
# нажать кнопку "Отправить"
# дождаться фидбека о том, что ответ правильный
# проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
#
# Правильным ответом на задачу в заданных шагах является число:
#
# import time
# import math
#
# answer = math.log(int(time.time()))
# Используйте маркировку pytest для параметризации и передайте в тест список ссылок в качестве параметров:
#
# https://stepik.org/lesson/236895/step/1
# https://stepik.org/lesson/236896/step/1
# https://stepik.org/lesson/236897/step/1
# https://stepik.org/lesson/236898/step/1
# https://stepik.org/lesson/236899/step/1
# https://stepik.org/lesson/236903/step/1
# https://stepik.org/lesson/236904/step/1
# https://stepik.org/lesson/236905/step/1
#
# Используйте осмысленное сообщение об ошибке в проверке текста, а также настройте нужные ожидания, чтобы тесты
# работали стабильно.
#
# В упавших тестах найдите кусочки послания. Тест должен падать, если текст в опциональном фидбеке не совпадает со
# строкой "Correct!" Соберите кусочки текста в одно предложение и отправьте в качестве ответа на это задание.
#
# Важно! Чтобы пройти это задание, дополнительно убедитесь в том, что у вас установлено правильное локальное время (
# https://time.is/ru/). Ответ для каждой задачи нужно пересчитывать отдельно, иначе они устаревают.
#


import math
import time

import pytest
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(ChromeDriverManager().install())
    yield browser
    print("\nquit browser..")
    browser.quit()


lts = []


@pytest.mark.parametrize('numbers', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_funk(browser, numbers):
    browser.implicitly_wait(5)
    link = f'https://stepik.org/lesson/{numbers}/step/1'
    browser.get(link)
    inp = browser.find_element_by_css_selector("textarea")
    answer = math.log(int(time.time()))
    inp.send_keys(str(answer))
    clicks = browser.find_element_by_css_selector(".submit-submission")
    clicks.click()
    texts = browser.find_element_by_css_selector("pre")
    texts_1 = texts.text
    # if texts_1 != 'Correct!':
    #     lts.append(texts_1)
    assert 'Correct!' == texts_1, f'Подсказка = {texts_1}'
    print(f"Ответ: {''.join(lts)}")
