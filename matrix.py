import random
import time
import shutil
import sys

VERDE = "\033[92m"
VERDE_OSCURO = "\033[32m"
BLANCO = "\033[97m"
RESET = "\033[0m"
LIMPIAR = "\033[2J"
OCULTAR_CURSOR = "\033[?25l"
MOSTRAR_CURSOR = "\033[?25h"
MOVER = "\033[{fila};{columna}H"


caracteres = "01アイウエオカキクケコサシスセソ ｴｶｷﾑﾕﾗｾﾈｽﾀﾇﾍ0123456789"
mensajes = [
   "Hackeando la NASA... mentira, es mi Ubuntu",
    "Robando contraseñas... del WiFi de mi casa",
    "Conectando con Morfeo...",
    "Error 404: Neo no encontrado",
    "Despertando a Skynet...",
    "Compilando el universo...",
    "sudo apt install superpoderes",
    "Acceso denegado: eres demasiado humano",
    "Hola, Elliot... ¿sigues despierto?",
    "Controlando el sistema... o eso quiero creer",
    "Señor Robot, el servidor está respirando",
    "fsociety: donde el caos tiene contraseña",
    "Reiniciando el capitalismo... progreso: 1 %",
    "Conectando a la red oscura de Nueva York...",
    "¿Qué haría Elliot con este bug?",
    "rm -rf /corporate/greed",
    "El sistema te observa; sonríe para el registro",
    "Tu anonimato ha expirado",
    "Desencriptando los secretos de E Corp...",
    "Error: demasiada realidad para una sola sesión",
    "Night City no duerme; solo cambia de turno",
    "Buscando a Johnny Silverhand...",
    "V, el encargo salió mal otra vez",
    "Instalando cromo... garantía no incluida",
    "El Relic tiene más estabilidad que mi conexión",
    "Arasaka ha detectado actividad sospechosa",
    "Militech pregunta si tienes un minuto",
    "Edgerunner por la noche, empleado temporal de día",
    "Subiendo mi conciencia a la nube... sin copia de seguridad",
    "Night City: aquí hasta los sueños tienen precio",
    "Choomba, el sistema volvió a caerse",
    "Pon música; voy a enfrentarme a una corporación",
    "Mi implante cerebral necesita una actualización",
    "Buscando una salida del laberinto corporativo",
    "Un mal día para tener un sistema nervioso analógico",
    "Conectado al ciberespacio... café todavía desconectado",
    "El futuro llegó; olvidó traer privacidad",
    "Mi firewall tiene más límites que yo",
    "Has desbloqueado: paranoia de nivel corporativo",
    "El servidor pidió vacaciones en otra dimensión",
    "Ejecutando protocolo: fingir que todo está bajo control",
    "Detrás de cada pantalla hay otra pantalla",
    "Tu realidad necesita una actualización de firmware",
    "Modo hacker: capucha puesta, problema sin resolver",
    "El código compila; la vida sigue dando errores",
    "Buscando señales de vida en el canal de soporte",
    "Conectando con la Matrix... espera, se cayó el WiFi",
    "Desperté en el futuro y nadie actualizó el manual",
    "Mis pensamientos están protegidos por un CAPTCHA",
    "El algoritmo sabe lo que hice el martes",
    "Reescribiendo mi destino en Python",
    "sudo make me a sandwich, versión distópica",
    "Mi conciencia no acepta los términos y condiciones",
    "El último humano en línea debe apagar la luz",
    "Pantalla azul: humanidad no responde",
    "Recargando la ciudad desde un terminal olvidado",
    "La corporación te quiere; tus datos también",
    "Intrusión detectada: alguien creyó en el futuro",
    "Bloqueando anuncios, drones y malas decisiones",
    "Un glitch en la simulación y ya es lunes",
    "Mis sueños corren en una máquina virtual",
    "El destino tiene permisos de administrador",
    "Convirtiendo café en código y código en problemas",
    "Actualización disponible: instala más paciencia",
    "El dron de vigilancia también necesita terapia",
    "El futuro es brillante; el cielo está contaminado",
    "Contraseña incorrecta; identidad en duda",
    "El sistema funciona según lo previsto: nadie sabe por qué",
    "Entrando en modo fantasma...",
    "Tu perfil ha sido clasificado como anomalía",
    "La red recuerda lo que la ciudad intenta olvidar",
    "Descargando recuerdos... espacio insuficiente",
    "Buscando una salida que no esté detrás de un muro de pago",
    "Un hacker entra en un bar; el firewall pide identificación",
    "Este cuerpo funciona con café y software obsoleto",
    "Falla de seguridad: alguien dejó abierta la esperanza",
    "El ojo de la cámara parpadeó primero",
    "Conectando al servidor rebelde desde una tostadora",
    "Mis credenciales son secretas; mi escritorio no",
    "El futuro no tiene botón de deshacer",
    "Desactivando la vigilancia... en mi imaginación",
    "El código es poesía; el error, una crítica literaria",
    "Has entrado en la zona de cobertura de la distopía",
    "Viviendo en el borde de una actualización forzada",
    "Mi avatar tiene mejor estabilidad emocional",
    "La ciudad está en línea; yo, no tanto",
    "Conexión segura establecida con mis malas decisiones",
    "Buscando humanidad en la carpeta de descargas",
    "Los recuerdos están cifrados; la vergüenza no",
    "El sistema exige una contraseña más humana",
    "Sincronizando mi cerebro con el reloj del microondas",
    "El futuro me llamó; lo mandé al buzón de voz",
    "Firewall activado contra reuniones innecesarias",
    "Hoy soy una leyenda urbana con acceso limitado",
    "El megacorporativo dice que todo está bien",
    "Mi robot aspirador conoce demasiado sobre mí",
    "Abriendo un portal al escritorio remoto",
    "Neón, lluvia ácida y una tarea pendiente",
    "La resistencia empieza después de reiniciar",
    "El mundo terminó; la VPN sigue conectada",
    "Desbloqueando recuerdos que no pedí guardar",
    "Esta conversación será archivada por una máquina",
    "Una IA acaba de juzgar mi historial de pestañas",
    "Modo incógnito: la ilusión de tener secretos",
    "El sistema detectó sarcasmo; proceda con cautela",
    "¿Sueñan los androides con reiniciar el router?",
    "El futuro depende de una actualización de 3 GB",
    "Humanidad.exe dejó de responder",
    "Reinicia el mundo; conserva mis archivos",
    "Mi plan maestro necesita menos notificaciones",
    "El código fuente de la realidad está mal comentado",
    "Los robots heredarán la Tierra; yo les dejo la contraseña del WiFi",
    "Se busca copiloto para escapar de la simulación",
    "Fin de la transmisión: la ciudad sigue vigilando"
]


print("Entrando a la MATRIX...")
time.sleep(1)

print(OCULTAR_CURSOR + LIMPIAR)

try:
    while True:
        terminal = shutil.get_terminal_size()
        ancho = max(1, terminal.columns)
        alto = max(1, terminal.lines)

        # Una columna por cada 2 caracteres de ancho
        num_columnas = max(1, ancho // 2)

        # Crea o reinicia las columnas si cambia el tamaño de la terminal
        if 'columnas_matrix' not in globals() or len(columnas_matrix) != num_columnas:
            columnas_matrix = []

            for columna in range(num_columnas):
                columnas_matrix.append({
                    "x": columna * 2 + 1,
                    "y": random.randint(-alto, alto),
                    "velocidad": random.choice([1, 1, 2]),
                    "largo": random.randint(5, 15),
                })

        # Limpia la pantalla en cada fotograma
        print(LIMPIAR, end="")

        for dato in columnas_matrix:
            # Dibuja la estela
            for i in range(dato["largo"]):
                fila = dato["y"] - i

                if 1 <= fila <= alto:
                    caracter = random.choice(caracteres)

                    if i == 0:
                        color = BLANCO
                    elif i < 3:
                        color = VERDE
                    else:
                        color = VERDE_OSCURO

                    print(
                        MOVER.format(fila=fila, columna=dato["x"])
                        + color + caracter + RESET,
                        end="",
                    )

            # Avanza la columna hacia abajo
            dato["y"] += dato["velocidad"]

            # Si sale por abajo, reaparece arriba
            if dato["y"] - dato["largo"] > alto:
                dato["y"] = random.randint(-10, 0)
                dato["velocidad"] = random.choice([1, 1, 2])
                dato["largo"] = random.randint(5, 15)

        # Mensaje ocasional
        if random.random() < 0.005:
            fila = random.randint(2, alto - 2)
            columna = random.randint(2, max(2, ancho - 40))
            mensaje = random.choice(mensajes)

            print(
                MOVER.format(fila=fila, columna=columna)
                + VERDE + ">>> " + mensaje + RESET,
                end="",
            )

        # Velocidad general de la animación
        time.sleep(0.01)

except KeyboardInterrupt:
    print(MOSTRAR_CURSOR + RESET)
    print("\nMATRIX DESCONECTADA.")
    print("Neo ha abandonado el servidor.")
    print("Hasta la próxima, hacker.")
    sys.exit(0)
