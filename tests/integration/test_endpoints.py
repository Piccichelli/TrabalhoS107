import pytest
import requests

class TestEndpoints:

    def test_home(self):
        # FIXTURE
        url = 'http://127.0.0.1:7999'

        # EXERCISE
        result = requests.get(url)

        # ASSERTS
        assert result.status_code == 200
        assert result.json() == {'message': 'Hello World!'}

    def test_welcome(self):
        # FIXTURE
        name = 'Pedro'
        url = f'http://127.0.0.1:7999/{name}'

        # EXERCISE
        result = requests.get(url)

        # ASSERTS
        assert result.status_code == 200
        assert result.json() == {'message': 'Hello Pedro'}