import unittest 
from unittest.mock import patch 

from user_turn import user_turn, validate_number


class TestCaptureImport(unittest.TestCase): 
    @patch('user_turn.input')  
    def test_user_turn_input(self, mock_input): 
        mock_input.return_value = '25' 
        result = user_turn()   
        self.assertEqual(result, 25) 

class TestNotCaptureImport(unittest.TestCase): 
    @patch('user_turn.input')
    @patch('builtins.print')
    def test_user_turn_input(self, mock_input, mock_print): 
        mock_input.return_value = 'hola'
        user_turn()  
        mock_print.assert_called_with("Introduce un número: ") 
       
 
class TestValidateNumber(unittest.TestCase): 
    @patch('user_turn.input')  
    def test_user_turn_input(self, mock_input): 
        mock_input.return_value = '32' 
        user_number = user_turn()   
        result = validate_number(user_number) 
        self.assertEqual(result, 32) 

class TestNotValidateNumber(unittest.TestCase): 
    @patch('user_turn.input')  
    def test_user_turn_input(self, mock_input): 
        mock_input.return_value = '500' 
        user_number = user_turn()   
        result = validate_number(user_number) 
        self.assertEqual(result, "Ingresa un número valido") 

