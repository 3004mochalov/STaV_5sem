from main import Calculator
import unittest


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_fib(self):
        self.assertEqual(self.calculator.n_fib(7), 13)

    def test_fact(self):
        self.assertEqual(self.calculator.fact(7), 5040)


if __name__ == "__main__":
    unittest.main()
