import unittest
from unittest.mock import patch
from game import game

class TestGameSystem(unittest.TestCase):
    @patch('game.random_number')
    @patch('game.user_turn')   
    @patch('game.system_turn')     
    @patch('builtins.print')

    def test_game_system_win(self, mock_print, mock_system_turn, mock_user_turn, mock_random_number):
        mock_random_number.return_value = 75
        mock_user_turn.return_value = 35 
        mock_system_turn.return_value = 75 
        
        game()

        self.assertTrue(mock_print.called)
        self.assertEqual(mock_print.call_count, 5)

class TestGameUser(unittest.TestCase):
    @patch('game.random_number')
    @patch('game.user_turn')       
    @patch('builtins.print')

    def test_game_user_win(self, mock_print, mock_user_turn, mock_random_number):
        mock_random_number.return_value = 52
        mock_user_turn.return_value = 52
        
        
        game()
        print(mock_print)

        self.assertTrue(mock_print.called)
        self.assertEqual(mock_print.call_count, 4)
        




