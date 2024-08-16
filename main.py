from src.lib.random_number_function import random_number
from src.lib.user_turn_function import validate_number
from src.lib.system_turn_function import system_turn
from src.lib.comparison_function import comparison
from src.lib.record_number import record_numbers

user_list = []
system_list = []

def game():
    
    number = random_number()
    print(number)
    
     
    while True:

        user_number = validate_number()
        record_user = record_numbers(user_number, user_list)

        if user_number == number:
            print("correcto!! acertaste el numero")
            print()
            print(f"Registro de números {record_user}")
            print()

            break
        else: comparison(user_number, number)
        print()
        print("------------system turn--------------")
        print()
       
        system_number = system_turn()
        record_system = record_numbers(system_number, system_list)

        if system_number == number:
            print("correcto!! acertaste el numero")
            print()
            print(record_system)
            print()
            break
        else: comparison(system_number, number)
        print()
        print("-------------user turn----------------")
        print()


game()
