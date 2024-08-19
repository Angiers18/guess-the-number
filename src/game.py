from random_number import random_number
from user_turn import user_turn, validate_number
from system_turn import system_turn
from comparison import comparison
from record_number import record_numbers

user_list = []
system_list = []

def game():
 
    number = random_number()
    print(number)
    
     
    while True:
        print("-------------user turn----------------")
        user_number = user_turn()
        validate_number(user_number)
        record_user = record_numbers(user_number, user_list)

        if user_number == number:
            print("correcto!! acertaste el numero")
            print(f"Registro de números {record_user}")

            break
        else: comparison(user_number, number)
        print("------------system turn--------------")
      
       
        system_number = system_turn()
        record_system = record_numbers(system_number, system_list)

        if system_number == number:
            print("correcto!! acertaste el numero")
            print(f"Registro de números {record_system}")
            break
        else: comparison(system_number, number)
        

game()