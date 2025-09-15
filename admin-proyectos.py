import os
import json

# Lista principal que almacena todos los proyectos
# Cada proyecto es una lista: [nombreProyecto, nombreResponsable, estado, avance]
proyectos = []

salir = ''

while True:
    os.system('cls')

    print(" Agenda de proyectos")
    print("1.- Crear proyecto")
    print("2.- Leer proyectos")
    print("3.- Actualizar proyecto")
    print("4.- Eliminar proyecto")
    print("5.- Buscar proyecto")
    print("6.- Guardar agenda en JSON")
    print("7.- Recuperar agenda desde JSON")
    print("8.- Salir")
    
    opcion = input("\nElegir una opcion: ").strip()
    
    match opcion:
        case "1":
            print("Usted selecciono la opcion: ", opcion)
            
            nombreProyecto = input("\nIngrese nombre del proyecto: ").strip()
            if not nombreProyecto:
                print("El nombre no puede estar vacío")
                input("\nPresiona ENTER para continuar...")
                continue
            
            nombreResponsable = input("\nIngrese el nombre del responsable: ").strip()
            if not nombreResponsable:
                print("El nombre del responsable no puede estar vacío")
                input("\nPresiona ENTER para continuar...")
                continue
            
            estado = input("\nTipo de estado: \n1.-Pendiente \n2.-En progreso \n3.-Finalizado \nIngrese el estado: ").strip()
            estados_validos = {"1": "Pendiente", "2": "En progreso", "3": "Finalizado"}
            if estado not in ["1", "2", "3"]:
                print("Estado inválido")
                input("\nPresiona ENTER para continuar...")
                continue
            estado = estados_validos[estado]
            
            avance = input("Ingrese el avance logrado (0-100): ").strip()
            if not avance.isdigit() or not (0 <= int(avance) <= 100):
                print("Avance inválido")
                input("\nPresiona ENTER para continuar...")
                continue
            
            proyectos.append([nombreProyecto, nombreResponsable, estado, int(avance)])
            input("\nPresiona ENTER para continuar...")
        
        case "2":
            print("Usted selecciono la opcion: ", opcion)
            if len(proyectos) == 0:
                print("No hay proyectos registrados")
            else:
                for i, proj in enumerate(proyectos, start=1):
                    nombreProyecto, nombreResponsable, estado, avance = proj
                    barra = "█" * (avance // 10) + "-" * (10 - avance // 10)
                    print(f"{i} .- Nombre: {nombreProyecto} - Responsable: {nombreResponsable} - Estado: {estado} - Avance: [{barra}] {avance}%")
            input("\nPresiona ENTER para continuar...")
        
        case "3":
            print("Usted selecciono la opcion: ", opcion)
            if len(proyectos) == 0:
                print("No hay proyectos registrados")
                input("\nPresiona ENTER para continuar...")
                continue
            
            nombreProyecto = input("\nIngrese el nombre del proyecto a actualizar: ").strip()
            # Buscar proyecto
            index = next((i for i, p in enumerate(proyectos) if p[0] == nombreProyecto), None)
            if index is None:
                print("El proyecto no existe")
                input("\nPresiona ENTER para continuar...")
                continue
            
            proj = proyectos[index]
            print(f"\nDatos actuales: Nombre: {proj[0]}, Responsable: {proj[1]}, Estado: {proj[2]}, Avance: {proj[3]}%")
            
            newNombre = input("Nuevo nombre (ENTER para no cambiar): ").strip()
            if newNombre:
                proj[0] = newNombre
            
            newResponsable = input("Nuevo responsable (ENTER para no cambiar): ").strip()
            if newResponsable:
                proj[1] = newResponsable
            
            newEstado = input("Nuevo estado (1-Pendiente, 2-En progreso, 3-Finalizado, ENTER para no cambiar): ").strip()
            estados_validos = {"1": "Pendiente", "2": "En progreso", "3": "Finalizado"}
            if newEstado:
                proj[2] = estados_validos.get(newEstado, proj[2])
            
            newAvance = input("Nuevo avance (0-100, ENTER para no cambiar): ").strip()
            if newAvance:
                if newAvance.isdigit() and 0 <= int(newAvance) <= 100:
                    proj[3] = int(newAvance)
                else:
                    print("Avance inválido. Se mantiene el anterior.")
            
            proyectos[index] = proj
            print("\nProyecto actualizado con éxito")
            input("\nPresiona ENTER para continuar...")
        
        case "4":
            if len(proyectos) == 0:
                print("No hay proyectos registrados")
                input("\nPresiona ENTER para continuar...")
                continue
            
            nombreProyecto = input("Ingrese nombre del proyecto a eliminar: ").strip()
            index = next((i for i, p in enumerate(proyectos) if p[0] == nombreProyecto), None)
            if index is None:
                print("El proyecto no existe")
                input("\nPresiona ENTER para continuar...")
                continue
            
            print(f"\nProyecto: {proyectos[index][0]} - Responsable: {proyectos[index][1]} - Estado: {proyectos[index][2]} - Avance: {proyectos[index][3]}%")
            confirm = input("¿Seguro que desea eliminar? (s/n): ").strip().lower()
            if confirm == 's':
                proyectos.pop(index)
                print("Proyecto eliminado")
            else:
                print("Operación cancelada")
            input("\nPresiona ENTER para continuar...")
        
        case "5":
            if len(proyectos) == 0:
                print("No hay proyectos registrados")
                input("\nPresiona ENTER para continuar...")
                continue
            
            nombreProyecto = input("Ingrese nombre del proyecto a buscar: ").strip()
            proj = next((p for p in proyectos if p[0] == nombreProyecto), None)
            if proj is None:
                print("El proyecto no existe")
            else:
                print(f"\nNombre: {proj[0]} - Responsable: {proj[1]} - Estado: {proj[2]} - Avance: {proj[3]}%")
            input("\nPresiona ENTER para continuar...")
        
        case "6":
            if len(proyectos) == 0:
                print("No hay proyectos para guardar")
            else:
                try:
                    with open("proyecto.json", "w", encoding="utf-8") as f:
                        json.dump(proyectos, f, indent=4, ensure_ascii=False)
                    print("Agenda guardada correctamente")
                except Exception as e:
                    print(f"Error al guardar: {e}")
            input("\nPresiona ENTER para continuar...")
        
        case "7":
            try:
                with open("proyecto.json", "r", encoding="utf-8") as f:
                    proyectos = json.load(f)
                print("Agenda recuperada correctamente")
                if len(proyectos) == 0:
                    print("La agenda está vacía")
                else:
                    for proj in proyectos:
                        print(f"\nNombre: {proj[0]} - Responsable: {proj[1]} - Estado: {proj[2]} - Avance: {proj[3]}%")
            except FileNotFoundError:
                print("No existe un archivo 'proyecto.json'. Guarde primero.")
            except json.JSONDecodeError:
                print("El archivo está dañado o vacío")
            except Exception as e:
                print(f"Error al recuperar: {e}")
            input("\nPresiona ENTER para continuar...")
        
        case "8":
            print("\n¿Seguro que desea salir de la Agenda de Proyectos?")
            salir = input("Escriba [s] para salir o [n] para volver al menú: ").strip().lower()
            if salir == "s":
                print("\nGracias por usar la Agenda de Proyectos. ¡Hasta luego!")
                break
            else:
                print("\nVolviendo al menú...")
                input("Presiona ENTER para continuar...")
        case _:
            print("Opción no válida")
            input("Presiona ENTER para continuar...")
