from random import randint

def random_number():
   
# Arroja un numero random entre 1 y 100 
    number = randint(1, 100)   
    return number

def comparison(guess, number):
    """
    compara la suposicion del jugador con el numero arrojado por el sistema

    parametros: 
    guess(int): suposicion de los jugadores
    number(int): numero que arroja el sistema
    """
    if guess < number:   
        print ("el número es mayor") 
    elif guess > number:   
        print ("el número es menor") 


def record_numbers(number, record_list):
    """
    introduce los numeros de los jugadores en una lista para llevar un registro

    parametros: 
    number(int): suposicion de los jugadores
    record_list([]): listas vacias donde se van introduciendo los numeros
    """
    record_list.append(number)
    return record_list

def start_game():
    #inicio de juego
    print("Bienvenido al juego Guess the Number")
    print("Adivina un numero al azar entre el 1 y 100")


def end_game(winner, record_list):
    """
    fin del juego

    parametros: 
    winner(str): quien gano el usuario o la computadora
    record_list([]): lista de registro del ganador
    """
    print(f"correcto!! {winner} acertaste el numero")
    print(f"Registro de números {record_list}")
