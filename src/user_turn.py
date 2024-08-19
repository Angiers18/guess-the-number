def user_turn(): 
    while True:  
        #captura numero de usuario   
        input_number = input("Introduce un número: ")  

        try: 
            user_number = int(input_number)  
            return user_number 

        except ValueError: 
            print("Ingresa un numero")
           
            

def validate_number(number): 
    if number < 1 or number > 100:  
        print("Ingresa un número dentro del rango") 
        return "Ingresa un número valido" 
    return number 
