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
    
        # Pedir al usuario que ingrese una opción
    opcion = input("\nElegir una opcion: ")
    
    match opcion:
        case "1":
            print("Usted selecciono la opcion: ", opcion)
            nombreProyecto = input("\nIngrese nombre del proyecto: ").strip()
            if not nombreProyecto:
                print("EL nombre no puede estar vacio")
                input("\nPresiona ENTER para continuar...")
                continue

            nombreResponsable = input("\nIngrese el nombre del responsable:").strip()
            if not nombreResponsable:
                print("EL nombre del responsable no puede estar vacio")
                input("\nPresiona ENTER para continuar...")
                continue
            estado = input("\nTipo de estado: \n1.-Pendiente \n2.-En progreso \n3.-Finalizado \nIngrese el estado: ").strip()
            estados_validos = {"1": "Pendiente", "2": "En progreso", "3": "Finalizado"}

            if estado not in ["1", "2", "3"]:
                print("Estado inválido")
                input("\nPresiona ENTER para continuar...")
                continue
            estado = estados_validos[estado]

            avance = input("Ingrese el avance logrado: ").strip()
            if not avance.isdigit() or not (0 <= int(avance) <= 100):
                print("EL avance no puede estar vacio")
                input("\nPresiona ENTER para continuar...")
                continue
                
            proyecto[nombreProyecto] = {"nombreResponsable": nombreResponsable, "estado": estado, 'avance': f"{avance}%"}
            
            input("\nPresiona ENTER para continuar...")
        case "2":
            print("Usted selecciono la opcion: ", opcion)
            if len(proyecto) == 0:
                print("No hay proyectos registrados")
                input("\nPresiona ENTER para continuar...")

            else:
                i=1
                for nombreProyecto, datos in proyecto.items():
                    
                    avance_num = int(avance)
                    barra = "█" * (avance_num // 10) + "-" * (10 - avance_num // 10)
                    print(i, ".-", "Nombre del proyecto:", nombreProyecto, 
                        "- Nombre del responsable:", datos["nombreResponsable"], 
                        "- Estado:", datos["estado"],
                        f"Avance logrado: [{barra}] {avance_num}%")
                    i += 1
                    input("\nPresiona ENTER para continuar...")
        case _:
            print("Opción NO válida. Intente nuevamente")
            input("Presione ENTER para continuar ...")