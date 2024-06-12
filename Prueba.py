import random
import os
#Soy Jefferson Mejia
# Colores para la salida
class Colores:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def jugar_adivina_el_numero():
    limpiar_pantalla()
    print(f"{Colores.HEADER}{Colores.BOLD}¡Bienvenido al juego de Adivina el Número!{Colores.ENDC}")
    nombre = input("¿Cuál es tu nombre? ")
    
    mejores_puntajes = {}

    while True:
        limpiar_pantalla()
        print(f"{Colores.OKCYAN}Hola, {nombre}. Elige un nivel de dificultad:{Colores.ENDC}")
        print("1. Fácil (1-50)")
        print("2. Medio (1-100)")
        print("3. Difícil (1-200)")
        
        while True:
            try:
                nivel = int(input("Introduce el nivel (1-3): "))
                if nivel in [1, 2, 3]:
                    break
                else:
                    print(f"{Colores.WARNING}Por favor, introduce un número válido (1-3).{Colores.ENDC}")
            except ValueError:
                print(f"{Colores.FAIL}Entrada no válida. Por favor, introduce un número entero.{Colores.ENDC}")

        if nivel == 1:
            rango = 50
        elif nivel == 2:
            rango = 100
        else:
            rango = 200
        
        numero_secreto = random.randint(1, rango)
        intentos = 0
        print(f"{Colores.OKCYAN}Estoy pensando en un número entre 1 y {rango}.{Colores.ENDC}")

        while True:
            try:
                intento = int(input("Introduce tu intento: "))
                intentos += 1

                if intento < 1 or intento > rango:
                    print(f"{Colores.WARNING}Por favor, introduce un número entre 1 y {rango}.{Colores.ENDC}")
                    continue

                if intento < numero_secreto:
                    print(f"{Colores.WARNING}Demasiado bajo. Intenta de nuevo.{Colores.ENDC}")
                elif intento > numero_secreto:
                    print(f"{Colores.WARNING}Demasiado alto. Intenta de nuevo.{Colores.ENDC}")
                else:
                    print(f"{Colores.OKGREEN}¡Felicidades, {nombre}! Has adivinado el número en {intentos} intentos.{Colores.ENDC}")
                    if nombre in mejores_puntajes:
                        if intentos < mejores_puntajes[nombre]:
                            mejores_puntajes[nombre] = intentos
                    else:
                        mejores_puntajes[nombre] = intentos
                    break
            except ValueError:
                print(f"{Colores.FAIL}Entrada no válida. Por favor, introduce un número entero.{Colores.ENDC}")

        print(f"{Colores.OKBLUE}Tu mejor puntaje: {mejores_puntajes[nombre]} intentos.{Colores.ENDC}")
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ")
        if jugar_de_nuevo.lower() != 's':
            print(f"{Colores.HEADER}{Colores.BOLD}¡Gracias por jugar, {nombre}! Hasta la próxima.{Colores.ENDC}")
            break

if __name__ == "__main__":
    jugar_adivina_el_numero()
