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
                'avance': int(avance)} # Avance en formato texto con "%"
            
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
                    convertAvance = datos["avance"]
                    avance_num = int(convertAvance)
                    
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
        case "3":
            # Caso 3: Actualizar un proyecto creado por su nombre
            print("Usted selecciono la opcion: ", opcion)
            
            # Verificamos si hay proyectos en la agenda
            if len(proyecto) == 0:
                print("No hay proyectos registrados")
                input("\nPresiona ENTER para continuar...")
                continue
            
            # Pedimos el nombre del proyecto a actualizar                                    
            nombreProyecto = input("\nIngrese el nombre del proyecto a actualizar: ").strip()
            
            # Validamos si el proyecto existe
            if nombreProyecto not in proyecto:
                print(" El proyecto no existe en la agenda.")
                input("\nPresiona ENTER para continuar...")
                continue
                        # Recuperamos los datos actuales del proyecto
            datos = proyecto[nombreProyecto]
            
                        # Mostramos la información actual del proyecto
            print(f"\n Datos actuales del proyecto '{nombreProyecto}':")
            print(f"- Responsable: {datos['nombreResponsable']}")
            print(f"- Estado: {datos['estado']}")
            print(f"- Avance: {datos['avance']}%")
            input("\nPresiona ENTER para continuar...")
            
            #Actualizar nombre del proyecto si lo desea
            newNombreProyecto = input("Ingrese nuevo nombre del proyecto (de no ser asi, ENTER): ").strip()
            if newNombreProyecto:
                # Borramos la clave antigua y asignamos la nueva
                proyecto[newNombreProyecto] = proyecto.pop(nombreProyecto)
                nombreProyecto = newNombreProyecto  # Actualizamos el nombre actual
                datos = proyecto[nombreProyecto]    # Referencia al diccionario actualizado
            # Actualizar nombre del responsable si lo desea
            newNombreResponsable = input("Ingrese nuevo nombre del responsable (de no ser asi, ENTER): ").strip()
            if newNombreResponsable:
                datos['nombreResponsable'] = newNombreResponsable
                
            # Actualizar estado del proyecto                
            newEstado = input("\nTipo de estado (de no ser asi, ENTER): \n1.-Pendiente \n2.-En progreso \n3.-Finalizado \nIngrese el estado: ").strip()             
            
            # Validamos que el estado ingresado sea correcto                        
            if newEstado:# Solo si ingresó algo
                newEstados_validos = {"1": "Pendiente", "2": "En progreso", "3": "Finalizado"}
            
                newEstado = newEstados_validos[newEstado]
                
                datos['estado'] = newEstado
                
            # Actualizar avance del proyecto
            newAvance = input("Ingrese el avance logrado (de no ser asi, ENTER): ").strip()
            if newAvance:
                if newAvance.isdigit() and 0 <= int(newAvance) <= 100:
                    datos["avance"] = int(newAvance) # Guardamos como porcentaje para mantener consistencia
                else:
                    print("Avance inválido. Se mantiene el anterior.")
                    
            # Guardamos los cambios en el diccionario principal                    
            proyecto[nombreProyecto] = datos
            
            # Confirmación de actualización
            print("\nProyecto actualizado con éxito.")
            print(datos)  # Mostramos el proyecto actualizado

            input("\nPresiona ENTER para continuar...")
            
        case "4":
            if len(proyecto) == 0:
                print("No hay proyectos registrados")
                input("\nPresiona ENTER para continuar...")
                continue
            
            eliminarProyecto = input("Ingrese nombre de proyecto a eliminar: ").strip()
            
            if eliminarProyecto not in proyecto:
                print(" El proyecto no existe en la agenda.")
                input("\nPresiona ENTER para continuar...")
                continue
            # Recuperamos los datos actuales del proyecto
            datos = proyecto[eliminarProyecto]
            
            # Mostramos la información actual del proyecto
            print(f"\n Datos actuales del proyecto '{eliminarProyecto}':")
            print(f"- Responsable: {datos['nombreResponsable']}")
            print(f"- Estado: {datos['estado']}")
            print(f"- Avance: {datos['avance']}%")
            print(datos)  # Muestra el diccionario completo (útil para depuración)
            input("\nPresiona ENTER para continuar...")
            
            opcionEliminar = input(f"\n¿Seguro que desea eliminar? \n1.- Sí \n2.- No \nElegir: ").strip()
            
            if opcionEliminar == "1":
                    proyecto.pop(eliminarProyecto)
                    print("\nProyecto eliminado correctamente")
            else:
                        print("\nOperación cancelada.")
            input("\nPresiona ENTER para continuar...")
        case "5":
            
            if len(proyecto) == 0:
                print("No hay proyectos registrados")
                input("\nPresiona ENTER para continuar...")
                continue
            
            buscarProyecto = input("\n Ingrese nombre de proyecto a buscar: ")
            
            if buscarProyecto not in proyecto:
                print(" El proyecto no existe en la agenda.")
                input("\nPresiona ENTER para continuar...")
                continue
            
            datosBuscar = proyecto[buscarProyecto]
            
            print(f"\n Nombre del proyecto: {buscarProyecto} \n Nombre del responsable: {datosBuscar['nombreResponsable']} \n Estado: {datosBuscar['estado']} \n Avance: {datosBuscar['avance']}%")
        case "6":
            if len(proyecto) == 0:
                print("No hay proyectos para guardar.")
            else:
                try:
                    with open("proyecto.json", "w", encoding="utf-8") as f:
                        json.dump(proyecto, f, indent=4, ensure_ascii=False)
                    print("\nAgenda guardada correctamente en 'proyecto.json'")
                    input("\nPresiona ENTER para continuar...")
                except Exception as e:
                    print(f"Error al guardar: {e}")
                    input("\nPresiona ENTER para continuar...")
        case "7":
                try:
                    with open("proyecto.json", "r", encoding="utf-8") as f:
                        proyecto = json.load(f)
                    print("\nAgenda recuperada correctamente desde 'proyecto.json'")
                    
                            # Mostrar todos los proyectos recuperados
                    if len(proyecto) == 0:
                        print("La agenda está vacía.")
                    else:
                        print("\nProyectos en la agenda:")
                    for nombre, datos in proyecto.items():
                        print(f"\n- Proyecto: {nombre}")
                        print(f"  Responsable: {datos['nombreResponsable']}")
                        print(f"  Estado: {datos['estado']}")
                        print(f"  Avance: {datos['avance']}%")
                        
                except FileNotFoundError:
                    print("No existe un archivo 'proyecto.json'. Guarde el proyecto primero.")
                except json.JSONDecodeError:
                    print("El archivo 'proyecto.json' está dañado o vacío.")
                except Exception as e:
                    print(f"Error al recuperar: {e}")
                input("\nPresiona ENTER para continuar...")            
        case _:
            # Caso por defecto: cuando la opción no coincide con ninguna válida
            print("Opción NO válida. Intente nuevamente")
            input("Presione ENTER para continuar ...")