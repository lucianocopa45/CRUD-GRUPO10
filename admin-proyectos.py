# Importamos librerías necesarias
import os      # Sirve para interactuar con el sistema operativo (ej: limpiar la consola).
import json    # Sirve para trabajar con archivos JSON (guardar y recuperar proyectos).

# Variable que almacena la opción elegida del menú.
# Comienza como cadena vacía y se actualiza con cada input del usuario.
opcion = ''
# Diccionario donde se van a almacenar todos los proyectos creados.
# Estructura: { nombreProyecto: { "nombreResponsable": str, "estado": str, "avance": str } }
proyecto = {}

salir = ''

# Bucle principal: se repite mientras la opción no sea "8" (que significa salir).
while True:
    os.system('cls')  # Limpiar la consola (solo Windows)

    # Mostrar las opciones del menú
    print(" Agenda de proyectos")
    print("1.- Crear proyecto")
    print("2.- Leer proyectos")
    print("3.- Actualizar proyecto")
    print("4.- Eliminar proyecto")
    print("5.- Buscar proyecto")
    print("6.- Guardar agenda en JSON")
    print("7.- Recuperar agenda desde JSON")
    print("8.- Salir")


