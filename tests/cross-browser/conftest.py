from pytest import fixture
from selenium import webdriver

@fixture(params=[webdriver.Chrome, webdriver.Firefox])
def browser(request):
    driver = request.param
    drvr = driver()
    yield drvr
    drvr.quit()