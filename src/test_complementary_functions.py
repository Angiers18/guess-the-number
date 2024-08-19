import unittest 
from unittest.mock import patch 

from comparison import comparison

class TestComparisonNumberLow(unittest.TestCase):
    @patch('builtins.print')
    def test_comparison(self, mock_print):
        guess = 18
        number = 54
        comparison(guess, number)
        mock_print.assert_called_with("el número es mayor")

class TestComparisonNumberHigh(unittest.TestCase):
    @patch('builtins.print')
    def test_comparison(self, mock_print):
        guess = 38
        number = 7
        comparison(guess, number)
        mock_print.assert_called_with("el número es menor")



