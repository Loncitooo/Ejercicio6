import random

def jugar_juego():
    print("¡Bienvenido al juego de adivinanza de números!")
    
    while True:
        try:
            rango_inferior = int(input("Por favor, ingresa el rango inferior de números: "))
            rango_superior = int(input("Por favor, ingresa el rango superior de números: "))
            if rango_inferior >= rango_superior:
                print("El rango inferior debe ser menor que el rango superior. Inténtalo de nuevo.")
            else:
                break
        except ValueError:
            print("Por favor, ingresa números válidos para el rango.")

    numero_secreto = random.randint(rango_inferior, rango_superior)
    intentos = 0
    puntuacion = 100

    print(f"Estoy pensando en un número entre {rango_inferior} y {rango_superior}.")

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
                print(f"Tu puntuación final es: {puntuacion}")
                break

            # Deduct points for each guess
            puntuacion -= 10
        except ValueError:
            print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    jugar_juego()
