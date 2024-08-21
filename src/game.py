from complementary_functions import  random_number, comparison, record_numbers, end_game
from user_turn import user_turn, validate_number
from system_turn import system_turn


user_list = []
system_list = []

def game():
 
    number = random_number()
    
     
    while True:
        print("-------------user turn----------------")
        user_number = user_turn()
        validate_number(user_number)
        record_user = record_numbers(user_number, user_list)

        if user_number == number:
           end_game('Usuario', record_user)
           break

        else: comparison(user_number, number)

        print("------------system turn--------------")
        system_number = system_turn()
        record_system = record_numbers(system_number, system_list)

        if system_number == number:
            end_game('Sistema', record_system)
            break
        
        else: comparison(system_number, number)
        
if __name__ == '__main__':
    game()