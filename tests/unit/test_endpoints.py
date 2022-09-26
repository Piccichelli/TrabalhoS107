from app.api import home, welcome, calculadora

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

    def test_calculator_valid_denominator(self):
        # FIXTURE
        a = 5
        b = 2

        # EXERCISE
        result = calculadora(a, b)

        # ASSERTS
        assert result == {"resultado": 2.5}

    def test_calculator_invalid_denominator(self):
        # FIXTURE
        a = 5
        b = 0

        # EXERCISE
        result = calculadora(a, b)

        # ASSERTS
        assert result == {"error": "Denominador inválido"}