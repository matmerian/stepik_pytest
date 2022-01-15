import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
	
	parser.addoption('--language', action='store', default=None, help="Type language name to select")

@pytest.fixture(scope="function")
def browser(request):
    my_language = request.config.getoption("--language")
    print("\nstart browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': my_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
    