from random import randrange


def system_turn():
#arroja un numero aleatorio del sistema  
    system_number = randrange(1, 100, 1)    
    system_decision = f"El número del sistema es {system_number}"
    print(system_decision)
    return system_number