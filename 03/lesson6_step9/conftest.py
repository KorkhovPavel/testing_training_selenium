from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    print("\nstart chrome browser for test..")
    yield browser
    print("\nquit browser..")
    browser.quit()
