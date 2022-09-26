import pytest
from app.api import home, welcome

class TestEndpoint:
    def test_home(self):
        # FIXTURE

        # EXERCISE
        result = home()

        # ASSERTS
        assert result == {'message': 'Hello World!'}

    def test_welcome(self):
        # FIXTURE
        name = 'Pedro'

        # EXERCISE
        result = welcome(name)

        # ASSERTS
        assert result == {'message': 'Hello Pedro'}