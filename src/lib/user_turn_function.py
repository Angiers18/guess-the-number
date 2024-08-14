def user_turn():
#captura numero de usuario  
    input_number = input("Introduce un número entre 1 y 100: ") 
    user_number = int(input_number) 
    return user_number
   

def validate_number():
    try:
        user_number = user_turn()
        if user_number < 1 or user_number > 100: 
            print("Ingresa un número valido")
            return None
    except ValueError:
            print("Ingresa un número")
            return None
    return user_number
