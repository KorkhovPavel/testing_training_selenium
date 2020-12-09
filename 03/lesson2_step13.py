from selenium import webdriver
import time
import unittest
from webdriver_manager.chrome import ChromeDriverManager


class TestUniSel(unittest.TestCase):
    def test_link_01(self):
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get('http://suninjuly.github.io/registration1.html')
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
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        time.sleep(10)
        browser.quit()

    def test_link_02(self):
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get('http://suninjuly.github.io/registration2.html')
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
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        time.sleep(10)
        browser.quit()


if __name__ == "__main__":
    unittest.main()
