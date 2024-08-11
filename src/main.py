# import random de donde se está exportando?? -- sin eso arroja un error  
import random 

def user_turn():

#arroja un numero aleatorio entre 1 y 100 
    number = random.randint(1, 100)  
    print(number) 

#captura numero de usuario  
    input_number = input("Introduce un número entre 1 y 100: ") 
    user_number = int(input_number)  

#comparacion   
    if user_number < number:   
        print ("el número es mayor") 
    elif user_number > number:   
        print ("el número es menor") 
    else: 
        print ("correcto!! acertaste el numero") 


user_turn() 
