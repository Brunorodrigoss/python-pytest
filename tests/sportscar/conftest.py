from pytest import fixture

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@fixture(scope='function')
def chrome_browser():
    service = Service(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    yield browser