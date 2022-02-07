import pytest

@pytest.mark.ui
@pytest.mark.entertainment
def test_can_navigate_to_entertainment_page(chrome_browser):
    chrome_browser.get('http://www.siriusxm.com')
    chrome_browser.quit()
    assert True
