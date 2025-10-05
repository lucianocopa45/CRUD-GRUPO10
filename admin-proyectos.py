# Importamos librerías necesarias
import os   # Para interactuar con el sistema operativo (ej: limpiar la consola)
import json # Para guardar y recuperar la agenda de proyectos en formato JSON
import random
import pandas as pd

# Lista principal que almacena todos los proyectos
# Cada proyecto es una lista con 4 elementos: [nombreProyecto, nombreResponsable, estado, avance]
proyectos = []

datos = []

entradaDatos = 0

# Variable para confirmar salida del programa
salir = ''

# Diccionario para mapear números a estados del proyecto
estados_validos = {1: "Pendiente", 2: "En progreso", 3: "Finalizado"}

# Bucle principal del programa: se ejecuta hasta que el usuario decida salir
while True:
    os.system('cls')  # Limpiar la consola en Windows

    # Mostrar el menú principal
    print(" Agenda de proyectos")
    print("1.- Crear proyecto")
    print("2.- Leer proyectos")
    print("3.- Actualizar proyecto")
    print("4.- Eliminar proyecto")
    print("5.- Buscar proyecto")
    print("6.- Guardar agenda en JSON")
    print("7.- Recuperar agenda desde JSON")
    
    # Pedimos al usuario que elija una opción
    opcion = input("\nElegir una opcion: ").strip()
    
    # match-case permite ejecutar un bloque según la opción elegida
    match opcion:
        case "1":
            # --- CREAR PROYECTO ---
            print("Usted seleccionó la opción: ", opcion)
            
            # Solicitar nombre del proyecto y validar que no esté vacío
            nombreProyecto = input("\nIngrese nombre del proyecto: ").strip()
            if not nombreProyecto:
                print("El nombre no puede estar vacío")
                input("\nPresiona ENTER para continuar...")
                continue
            
            # Solicitar nombre del responsable y validar
            nombreResponsable = input("\nIngrese el nombre del responsable: ").strip()
            if not nombreResponsable:
                print("El nombre del responsable no puede estar vacío")
                input("\nPresiona ENTER para continuar...")
                continue
            
            # Solicitar estado mediante número (1-3)
            estado = int(input("\nTipo de estado: \n1.-Pendiente \n2.-En progreso \n3.-Finalizado \nIngrese el estado: ").strip())
            
            # Validar estado ingresado
            if estado not in [1, 2, 3]:
                print("Estado inválido")
                input("\nPresiona ENTER para continuar...")
                continue
            # Convertir número a texto
            estado = estados_validos[estado]
            
            # Solicitar avance del proyecto (0-100)
            avance = input("Ingrese el avance logrado (0-100): ").strip()
            if not avance.isdigit() or not (0 <= int(avance) <= 100):
                print("Avance inválido")
                input("\nPresiona ENTER para continuar...")
                continue
            
            # Guardamos el proyecto como una lista en la lista principal
            proyectos.append([nombreProyecto, nombreResponsable, estado, int(avance)])
            
            input("\nPresiona ENTER para continuar...")

        case "2":
            # --- LEER PROYECTOS ---
            print("Usted seleccionó la opción: ", opcion)
            
            if len(proyectos) == 0 and len(datos) == 0:
                print("No hay proyectos registrados")
            else:
            # Recorremos la lista de proyectos y mostramos cada uno
                print()            
                print("---------------------------------------Lista de proyectos--------------------------")
                print()
                print("{:<30} {:<25} {:<15} {:<15}".format("Proyecto", "Responsable", "Estado", "Avance"))
                print("-" * 90)
            for i, proj in enumerate(proyectos, start=1):
                
                nombreProyecto, nombreResponsable, estado, avance = proj
                avance = int(avance)  # aseguramos que sea entero
                # Creamos una barra de progreso visual de 10 bloques
                barra = "█" * (avance // 10) + "-" * (10 - avance // 10)
            
                # Colores según avance
                if avance < 40:
                    color = "\033[91m"  # Rojo
                elif avance < 70:
                    color = "\033[93m"  # Amarillo
                else:
                    color = "\033[92m"  # Verde
            
                barraColor = f"{color}{barra}\033[0m"
            
                # Mostramos toda la información
                print("{:<30} {:<25} {:<15} {:<3}% [{}]".format(
                    nombreProyecto,
                    nombreResponsable,
                    estado,
                    avance,
                    barraColor
                ))
                ##generarBarra(datos, "Lista de proyectos aleatorios")
            print()
            print("----------------------------------Lista de proyectos aleatorios--------------------------")
            print()
            print("{:<30} {:<25} {:<15} {:<15}".format("Proyecto", "Responsable", "Estado", "Avance"))
            print("-" * 90)
            for datosRandom in datos:
                avance = int(datosRandom["avance"])  # aseguramos que sea número
                barra = "█" * (avance // 10) + "-" * (10 - avance // 10)
                
                if avance < 40:
                    color = "\033[91m"  # Rojo
                elif avance < 70:
                    color = "\033[93m"  # Amarillo
                else:
                    color = "\033[92m"  # Verde
        
                barraColor = f"{color}{barra}\033[0m"
                
                print("{:<30} {:<25} {:<15} {:<3}% [{}]".format(
                    datosRandom["nombreProyecto"],
                    datosRandom["nombreResponsable"],
                    datosRandom["estado"],
                    avance,
                    barraColor
                    
                ))
            input("\nPresiona ENTER para continuar...")
        
        case "3":
            # --- ACTUALIZAR PROYECTO ---
            print("Usted seleccionó la opción: ", opcion)
            
            if len(proyectos) == 0:
                print("No hay proyectos registrados")
                input("\nPresiona ENTER para continuar...")
                continue
            
            # Solicitar nombre del proyecto a actualizar
            nombreProyecto = input("\nIngrese el nombre del proyecto a actualizar: ").strip()
            if not nombreProyecto:
                print("El nombre no puede estar vacío")
                input("\nPresiona ENTER para continuar...")
                continue
            # Buscar el proyecto en la lista usando enumerate y next
            # Esto devuelve el índice del proyecto o None si no existe
            index = next((i for i, p in enumerate(proyectos) if p[0] == nombreProyecto), None)
            if index is None:
                print("El proyecto no existe")          
                input("\nPresiona ENTER para continuar...")
                continue
            
            proj = proyectos[index]  # Obtenemos la lista del proyecto
            
            # Mostrar datos actuales
            print(f"\nDatos actuales: Nombre: {proj[0]}, Responsable: {proj[1]}, Estado: {proj[2]}, Avance: {proj[3]}%")
            
            # --- Actualización de campos ---
            # Actualizar nombre
            newNombre = input("Nuevo nombre (ENTER para no cambiar): ").strip()
            if newNombre:
                proj[0] = newNombre
            
            # Actualizar responsable
            newResponsable = input("Nuevo responsable (ENTER para no cambiar): ").strip()
            if newResponsable:
                proj[1] = newResponsable
            
            # Actualizar estado
            newEstado = input("Nuevo estado (1-Pendiente, 2-En progreso, 3-Finalizado, ENTER para no cambiar): ").strip()
            if newEstado:
                proj[2] = estados_validos.get(newEstado, proj[2]) # Si el número es inválido, se mantiene el estado anterior
            
            # Actualizar avance
            newAvance = input("Nuevo avance (0-100, ENTER para no cambiar): ").strip()
            if newAvance:
                if newAvance.isdigit() and 0 <= int(newAvance) <= 100:
                    proj[3] = int(newAvance)
                else:
                    print("Avance inválido. Se mantiene el anterior.")
            
            # Guardamos los cambios
            proyectos[index] = proj
            print("\nProyecto actualizado con éxito")
            input("\nPresiona ENTER para continuar...")
        
        case "4":
            # --- ELIMINAR PROYECTO ---
            if len(proyectos) == 0:
                print("No hay proyectos registrados")
                input("\nPresiona ENTER para continuar...")
                continue
            
            nombreProyecto = input("Ingrese nombre del proyecto a eliminar: ").strip()
            
            # Buscamos el proyecto por nombre
            index = next((i for i, p in enumerate(proyectos) if p[0] == nombreProyecto), None)
            if index is None:
                print("El proyecto no existe")
                input("\nPresiona ENTER para continuar...")
                continue
            
            # Mostrar datos antes de eliminar
            print(f"\nProyecto: {proyectos[index][0]} - Responsable: {proyectos[index][1]} - Estado: {proyectos[index][2]} - Avance: {proyectos[index][3]}%")
            
            # Confirmación de eliminación
            confirm = input("¿Seguro que desea eliminar? (s/n): ").strip().lower()
            if confirm == 's':
                proyectos.pop(index)  # Eliminamos el proyecto de la lista
                print("Proyecto eliminado")
            else:
                print("Operación cancelada")
            input("\nPresiona ENTER para continuar...")
        
        case "5":
            # --- BUSCAR PROYECTO ---
            if len(proyectos) == 0:
                print("No hay proyectos registrados")
                input("\nPresiona ENTER para continuar...")
                continue
            
            nombreProyecto = input("Ingrese nombre del proyecto a buscar: ").strip()
            # Buscamos el proyecto y obtenemos la lista si existe
            proj = next((p for p in proyectos if p[0] == nombreProyecto), None)
            if proj is None:
                print("El proyecto no existe")
            else:
                print(f"\nNombre: {proj[0]} - Responsable: {proj[1]} - Estado: {proj[2]} - Avance: {proj[3]}%")            
            input("\nPresiona ENTER para continuar...")
        
        case "6":
            # --- GUARDAR A JSON ---
            if len(proyectos) == 0 and len(datos) == 0:
                print("No hay proyectos para guardar")
            else:
                try:
                    
                    proyectos_dict = []
                    for p in proyectos:
                        proyectos_dict.append({
                            "nombreProyecto": p[0],
                            "nombreResponsable": p[1],
                            "estado": p[2],
                            "avance": p[3]
                        })
                        
                    ambasListas = proyectos_dict + datos
                    
                    with open("proyecto.json" , "w", encoding="utf-8") as f:
                        json.dump(ambasListas, f, indent=4, ensure_ascii=False)
                        
                    print("Agenda guardada correctamente")
                except Exception as e:
                    print(f"Error al guardar: {e}")
            input("\nPresiona ENTER para continuar...")
        
        case "7":
            # --- RECUPERAR DE JSON ---
            try:
                with open("proyecto.json", "r", encoding="utf-8") as f:
                    proyectos_dict = json.load(f)
                    
                    for d in proyectos_dict:
                        proyectos.append([
                            d["nombreProyecto"],
                            d["nombreResponsable"],
                            d["estado"],
                            d["avance"]  # ya es entero
                        ])
                        ##print(f"\nNombre: {nombreProyecto} - Responsable: {responsable} - Estado: {estado} - Avance: {avance}%")
                print("Agenda recuperada correctamente")
                if len(proyectos) == 0:
                    print("La agenda está vacía")
                else:
                    # Mostrar todos los proyectos cargados
                    for proj in proyectos:
                        nombreProyecto = proj["nombreProyecto"]
                        responsable = proj["nombreResponsable"]
                        estado = proj["estado"]
                        avance = proj["avance"]
                        print(f"\nNombre: {nombreProyecto} - Responsable: {responsable} - Estado: {estado} - Avance: {avance}%")
                
                    # for proj in proyectos:
                    #     print(f"\nNombre: {proj[0]} - Responsable: {proj[1]} - Estado: {proj[2]} - Avance: {proj[3]}%")
                    #     input("\nPresiona ENTER para continuar...")
            except FileNotFoundError:
                print("No existe un archivo 'proyecto.json'. Guarde primero.")
            except json.JSONDecodeError:
                print("El archivo está dañado o vacío")
            except Exception as e:
                print(f"Error al recuperar: {e}")
            
            input("\nPresiona ENTER para continuar...")
            
        case "8":
            # --- SALIR DEL PROGRAMA ---
            print("\n¿Seguro que desea salir de la Agenda de Proyectos?")
            salir = input("Escriba [s] para salir o [n] para volver al menú: ").strip().lower()
            if salir == "s":
                print("\nGracias por usar la Agenda de Proyectos. ¡Hasta luego!")
                break
            else:
                print("\nVolviendo al menú...")
                input("Presiona ENTER para continuar...")
        
        case _:
            # Opción no válida
            print("Opción no válida")
            input("Presiona ENTER para continuar...")
