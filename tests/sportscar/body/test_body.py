import pytest

@pytest.mark.body
class BodyTests:

    @pytest.mark.door
    def test_body_function_as_expected(self):
        assert True

    def test_bumper(self):
        assert True

    def test_windshield(self):
        assert True
