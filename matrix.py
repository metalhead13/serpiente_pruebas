import random
import time
import shutil
import sys

VERDE = "\033[92m"
VERDE_OSCURO = "\033[32m"
BLANCO = "\033[97m"
RESET = "\033[0m"

caracteres = "01アイウエオカキクケコサシスセソ"
mensajes = [
    "Hackeando la NASA... mentira, es mi Ubuntu",
    "Robando contrasenas... del WiFi de mi casa",
    "Conectando con Morfeo...",
    "Error 404: Neo no encontrado",
    "Despertando a Skynet...",
    "Compilando el universo...",
    "sudo apt install superpoderes",
    "Acceso denegado: eres demasiado humano",
]

print("Entrando a MATRIX...")
time.sleep(2)

contador = 0

try:
    while True:
        ancho = shutil.get_terminal_size().columns
        ancho = max(1, ancho)

        lluvia = "".join(
            random.choice(caracteres)
            for _ in range(ancho)
        )

        color = random.choice([VERDE, VERDE_OSCURO, BLANCO])

        print(color + lluvia + RESET)

        contador += 1

        if contador % 15 == 0:
            mensaje = random.choice(mensajes)
            print(f"\n{VERDE}>>> {mensaje}{RESET}\n")

        time.sleep(0.06)

except KeyboardInterrupt:
    print(f"\n{BLANCO}MATRIX DESCONECTADA.")
    print("Neo ha abandonado el servidor.")
    print("Hasta la proxima, hacker.{RESET}")
    sys.exit(0)

