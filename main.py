from src.lib.random_number_function import random_number
from src.lib.user_turn_function import validate_number
from src.lib.system_turn_function import system_turn
from src.lib.comparison_function import comparison

def game():
    
    number = random_number()
    print(number)
    
     
    while True:

        user_number = validate_number()

        if user_number == number:
            print("correcto!! acertaste el numero")
            break
        else: comparison(user_number, number)
        print()
        print("------------system turn--------------")
        print()
       
        system_number = system_turn()

        if system_number == number:
            print("correcto!! acertaste el numero")
            break
        else: comparison(system_number, number)
        print()
        print("-------------user turn----------------")
        print()


game()
