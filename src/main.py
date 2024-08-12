import random 

#arroja un numero aleatorio entre 1 y 100 
number = random.randint(1, 100)    
 
def user_turn():
#captura numero de usuario  
    input_number = input("Introduce un número entre 1 y 100: ") 
    global user_number
    user_number = int(input_number) 

#comparacion   
    if user_number < number:   
        print ("el número es mayor") 
    elif user_number > number:   
        print ("el número es menor") 


def system_turn():
#arroja un numero aleatorio del sistema  
    global system_number
    system_number = random.randrange(1, 100, 1)    
    system_decision = f"El numero del sistema es {system_number}"
    print(system_decision)

#comparacion   
    if system_number < number:   
        print ("el número es mayor") 
    elif system_number > number:   
        print ("el número es menor") 
 


user_turn() 
while True:
    if user_number == number:
        print("correcto!! acertaste el numero")
        break
    else: system_turn()

    if system_number == number:
        print("correcto!! acertaste el numero")
        break
    else: user_turn()



