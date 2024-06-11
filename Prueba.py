import random

def jugar_adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    print("¡Bienvenido al juego de Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 100.")

    while True:
        try:
            intento = int(input("Introduce tu intento: "))
            intentos += 1

            if intento < 1 or intento > 100:
                print("Por favor, introduce un número entre 1 y 100.")
                continue

            if intento < numero_secreto:
                print("Demasiado bajo. Intenta de nuevo.")
            elif intento > numero_secreto:
                print("Demasiado alto. Intenta de nuevo.")
            else:
                print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
                break
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero.")

    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ")
    if jugar_de_nuevo.lower() == 's':
        jugar_adivina_el_numero()
    else:
        print("¡Gracias por jugar! Hasta la próxima.")

if __name__ == "__main__":
    jugar_adivina_el_numero()
