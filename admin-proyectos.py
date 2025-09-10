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
    
    # match-case permite ejecutar un bloque de código dependiendo de la opción seleccionada.
    match opcion:
        case "1":
            # Caso 1: Crear un nuevo proyecto
            print("Usted selecciono la opcion: ", opcion)
            
            # Se pide el nombre del proyecto
            nombreProyecto = input("\nIngrese nombre del proyecto: ").strip()
            if not nombreProyecto: # Validación: no puede estar vacío
                print("EL nombre no puede estar vacio")
                input("\nPresiona ENTER para continuar...")
                continue # Vuelve al inicio del bucle
            
            # Se pide el nombre del responsable del proyecto
            nombreResponsable = input("\nIngrese el nombre del responsable:").strip()
            if not nombreResponsable: # Validación: no puede estar vacío
                print("EL nombre del responsable no puede estar vacio")
                input("\nPresiona ENTER para continuar...")
                continue
            
            # Se pide el estado del proyecto
            estado = input("\nTipo de estado: \n1.-Pendiente \n2.-En progreso \n3.-Finalizado \nIngrese el estado: ").strip()
            
            # Diccionario que mapea números a estados válidos
            estados_validos = {"1": "Pendiente", "2": "En progreso", "3": "Finalizado"}

            # Validar que el estado ingresado esté dentro de las opciones
            if estado not in ["1", "2", "3"]:
                print("Estado inválido")
                input("\nPresiona ENTER para continuar...")
                continue
            estado = estados_validos[estado] # Se reemplaza el número por el texto correspondiente

            # Se pide el avance del proyecto en porcentaje (0 a 100)
            avance = input("Ingrese el avance logrado: ").strip()
            
            # Validamos que sea un número y esté en el rango 0 a 100
            if not avance.isdigit() or not (0 <= int(avance) <= 100):
                print("EL avance no puede estar vacio")
                input("\nPresiona ENTER para continuar...")
                continue
            
            # Se guarda el proyecto en el diccionario principal "proyecto"
            proyecto[nombreProyecto] = {
                "nombreResponsable": nombreResponsable, # Responsable del proyecto
                "estado": estado,  # Estado actual
                'avance': f"{avance}%"} # Avance en formato texto con "%"
            
            # Pausa para que el usuario vea el resultado antes de volver al menú
            input("\nPresiona ENTER para continuar...")
        case "2":
            # Caso 2: Mostrar todos los proyectos creados
            print("Usted selecciono la opcion: ", opcion)
                        
            # Verificamos si hay proyectos en el diccionario
            if len(proyecto) == 0:
                print("No hay proyectos registrados")
                input("\nPresiona ENTER para continuar...")
            else:
                i=1 # Contador para enumerar los proyectos
                
                # Recorremos todos los proyectos del diccionario
                for nombreProyecto, datos in proyecto.items():
                    
                    # Obtenemos el avance como número (quitando el "%")
                    avance_num = int(avance)
                    
                    # Creamos una barra de progreso de 10 bloques
                    barra = "█" * (avance_num // 10) + "-" * (10 - avance_num // 10)
                    
                    # Mostramos la información del proyecto
                    print(i, ".-", "Nombre del proyecto:", nombreProyecto, 
                        "- Nombre del responsable:", datos["nombreResponsable"], 
                        "- Estado:", datos["estado"],
                        f"Avance logrado: [{barra}] {avance_num}%")
                    i += 1 # Incrementa el contador de proyectos
                    # Pausa para que el usuario pueda leer la información
                    input("\nPresiona ENTER para continuar...")
        case _:
            # Caso por defecto: cuando la opción no coincide con ninguna válida
            print("Opción NO válida. Intente nuevamente")
            input("Presione ENTER para continuar ...")