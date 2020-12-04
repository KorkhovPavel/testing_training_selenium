import math
import time

from selenium import webdriver


from webdriver_manager.chrome import ChromeDriverManager

link = " http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(link)
    links = browser.find_element_by_partial_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    links.click()
    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name('city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(30)
    browser.quit()
