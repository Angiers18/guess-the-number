def user_turn(): 
    while True:  
        """
        funcion que permite al usuario inroducir sus suposiciones 
        bucle que permite que se ingresen solo numeros enteros
        
        """   
        
        input_number = input("Introduce un número: ")  
        try: 
            user_number = int(input_number)  
            return user_number 

        except ValueError: 
            print("Ingresa un numero")
           
            

def validate_number(number): 

    """
    funcion valida que el numero ingresado este  
    dentro de los parametros establecidos
        
    """ 

    if number < 1 or number > 100:  
        print("Ingresa un número valido") 
        user_turn()
        return "Ingresa un número valido" 
    return number 
