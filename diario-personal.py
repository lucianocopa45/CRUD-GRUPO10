# Importamos librerías necesarias
import os      # Para limpiar la consola según el sistema operativo
import csv     # Para leer y escribir archivos CSV
import time  # Importamos el módulo 'time' para poder usar 'sleep' y crear efectos de animación


# Lista global que almacenará las entradas del diario
# Cada entrada es una lista: [fecha, título, contenido]
diario =  []
opcion =  ""

# Función para limpiar la consola según el sistema operativo
def limpiar_consola():
    os.system('cls'if os.name == 'nt' else 'clear') # cls para Windows, clear para Mac/Linux
    
    
# Función para pausar la ejecución hasta que el usuario presione Enter 
def pausar():
    input("\nPresiona Enter para continuar...")   #Espera la interaccion del usuario
    
# Función para mostrar el menú principal del diario
def mostrar_menu():
    limpiar_consola()  # Limpiamos la consola antes de mostrar el menú

    # Códigos de color ANSI para dar estilo al texto en consola
    RESET = "\033[0m"     # Restablece el color por defecto
    CYAN = "\033[96m"     # Color cian
    YELLOW = "\033[93m"   # Color amarillo
    GREEN = "\033[92m"    # Color verde
    MAGENTA = "\033[95m"  # Color magenta

    # Título con efecto de escritura letra por letra
    titulo = "✨📖  Bienvenido a tu Diario  📖✨"
    print(CYAN + "╔" + "═" * 40 + "╗" + RESET)  # Parte superior del recuadro del título
    print("║", end="")  # Comenzamos la línea del título sin salto de línea
    for letra in titulo.center(40):  # Centramos el título en 40 caracteres
        print(CYAN + letra + RESET, end="", flush=True)  # Imprime cada letra en cian, sin saltos
        time.sleep(0.02)  # Pausa breve para efecto de animación tipo “tecleo”
    print("║")  # Cierra la línea del recuadro del título
    print(CYAN + "╚" + "═" * 40 + "╝" + RESET)  # Parte inferior del recuadro del título

    # Lista de opciones del menú con colores y emojis
    opciones = [
        (GREEN, "1. ➕ Crear Diario"),
        (CYAN, "2. 📖 Ver Diarios"),
        (YELLOW, "3. ✏️ Actualizar Diario"),
        (MAGENTA, "4. 🗑️ Eliminar Diario"),
        (GREEN, "5. 🔍 Buscar Diario"),
        (CYAN, "6. 💾 Guardar Diario (CSV)"),
        (YELLOW, "7. 📂 Cargar Diario (CSV)"),
        (MAGENTA, "8. 🚪 Salir")
    ]
    

    # Separador animado superior del menú
    separador = "─" * 40  # Creamos una línea de 40 caracteres
    for char in separador:
        print(CYAN + char + RESET, end="", flush=True)  # Imprime cada guion con color cian
        time.sleep(0.05)  # Pausa muy breve para efecto animado
    print()  # Salto de línea al finalizar el separador

    # Imprimimos cada opción del menú con un pequeño retraso para efecto visual
    for color, opcion in opciones:
        print(color + opcion + RESET)  # Imprime la opción con su color correspondiente
        time.sleep(0.10)  # Pequeña pausa para efecto animación

    # Separador animado inferior del menú
    for char in separador:
        print(CYAN + char + RESET, end="", flush=True)  # Imprime cada guion con color cian
        time.sleep(0.010)  # Pausa breve
    print()  # Salto de línea al finalizar el separador
    