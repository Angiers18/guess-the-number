import unittest 
from unittest.mock import patch

from game import game

class TestGameComplete(unittest.TestCase):
    @patch('game.random_number')
    @patch('game.user_turn') 
    @patch('game.system_turn')

    def test_game_function(self, mock_user_turn, mock_system_turn, mock_random_number):

        mock_random_number.return_value = 75
        mock_user_turn.return_value = 75
        mock_system_turn.return_value = 38
        
        # Capturar la salida del print
        with patch('builtins.print') as mocked_print:
            game()
            # Verificar si el usuario ganó
            mocked_print.assert_called_with("Registro de números [75]")
            #mocked_print.assert_called_with("correcto!! acertaste el numero")
            

    if __name__ == '__main__':
        unittest.main()
    
