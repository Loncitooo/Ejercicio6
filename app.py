import random

def jugar_juego():
    numero_secreto = random.randint(1, 100)
    intentos = 0
#hace un print normal
    print("¡Bienvenido al juego de adivinanza de números!")
    print("Estoy pensando en un número entre 1 y 100.")

    while True:
        try:
            guess = int(input("¿Cuál crees que es ese número? "))
            intentos += 1

            if guess < numero_secreto:
                print("El número secreto es mayor. ¡Intenta de nuevo!")
            elif guess > numero_secreto:
                print("El número secreto es menor. ¡Intenta de nuevo!")
            else:
                print(f"¡Felicidades! Adivinaste el número secreto ({numero_secreto}) en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    jugar_juego()
