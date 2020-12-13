from googletrans import Translator
import time


def test_check_add_to_cart_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(30)
    btn = browser.find_element_by_css_selector("#add_to_basket_form")
    btn_text = btn.text
    translator = Translator()
    text_translator = translator.translate(btn_text)
    assert 'add to cart' == text_translator.text.lower(), f'Кнопка отсутсвует'
