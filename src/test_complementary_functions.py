import unittest 
from unittest.mock import patch 

from complementary_functions import comparison, end_game

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

class TestEndgame(unittest.TestCase):
    @patch('builtins.print') 
    def test_end_game(self, mock_print):
        winner = "Aurora"
        list_number = [51, 38, 22]

        end_game(winner, list_number)

        self.assertTrue(mock_print.called)

        self.assertEqual(mock_print.call_count, 2)



