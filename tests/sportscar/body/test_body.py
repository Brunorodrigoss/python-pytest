import pytest

@pytest.mark.smoke
@pytest.mark.body
class BodyTests:

    @pytest.mark.ui
    def test_can_navigate_to_body_page(self, chrome_browser):
        chrome_browser.get('http://www.motortrend.com/')
        chrome_browser.quit()
        assert True

    def test_bumper(self):
        assert True

    def test_windshield(self):
        assert True
