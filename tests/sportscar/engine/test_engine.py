import pytest

@pytest.mark.smoke
@pytest.mark.engine
@pytest.mark.ui
def test_can_navigate_to_engine_page(chrome_browser):
    chrome_browser.get('https://www.artofmanliness.com/articles/how-a-cars-engine-works/')
    chrome_browser.quit()
    assert True
