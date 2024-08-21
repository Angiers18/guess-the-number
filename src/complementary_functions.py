from random import randint

def random_number():
#arroja un numero aleatorio entre 1 y 100 
    number = randint(1, 100)   
    return number

def comparison(guess, number):
#comparar la susposicion de los juagadores con el numero aleatorio del sistema
    if guess < number:   
        print ("el número es mayor") 
    elif guess > number:   
        print ("el número es menor") 


def record_numbers(number, record_list):
    record_list.append(number)
    return record_list

def start_game():
    print("Bienvenido al juego Guess the Number")
    print("Adivia un numero al azar entre el 1 y 100")


def end_game(winner, record_list):
    print(f"correcto!! {winner} acertaste el numero")
    print(f"Registro de números {record_list}")
