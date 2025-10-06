# Importamos librerías necesarias
import os   # Para interactuar con el sistema operativo (ej: limpiar la consola)
import json # Para guardar y recuperar la agenda de proyectos en formato JSON
import random
import pandas as pd
from colorama import Fore, Style, init
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import time, sys
from datetime import datetime
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

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
    print("6.- Guardar proyectos en JSON")
    print("7.- Recuperar proyectos desde JSON")
    print("8.- Generar datos aleatorios")
    print("9.- Generar graficos")
    print("10.- Salir")
    
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
            # === OPCIÓN 5: BUSCAR PROYECTO ===
            # Verifica si hay proyectos cargados en la lista "proyectos".
            # Si no hay, muestra un mensaje y vuelve al menú principal.
            if len(proyectos) == 0:
                print("No hay proyectos registrados")
                input("\nPresiona ENTER para continuar...")
                continue
            
            # Solicita al usuario el nombre del proyecto a buscar.
            nombreProyecto = input("Ingrese nombre del proyecto a buscar: ").strip()
            
            # Busca dentro de la lista "proyectos" un proyecto cuyo primer elemento (nombre) coincida.
            # 'next' devuelve el primer resultado que cumpla la condición o None si no lo encuentra.
            proj = next((p for p in proyectos if p[0] == nombreProyecto), None)
            
            # Si no existe, lo informa al usuario.
            if proj is None:
                print("El proyecto no existe")
            else:
                # Si se encuentra, muestra todos los datos del proyecto.
                print(f"\nNombre: {proj[0]} - Responsable: {proj[1]} - Estado: {proj[2]} - Avance: {proj[3]}%")            
            input("\nPresiona ENTER para continuar...")
        
        
        case "6":
            # === OPCIÓN 6: GUARDAR PROYECTOS EN JSON ===
            # Esta opción guarda todos los proyectos en un archivo 'proyecto.json'.
            
            # Si no hay proyectos ni datos aleatorios generados, no hay nada que guardar.
            if len(proyectos) == 0 and len(datos) == 0:
                print("No hay proyectos para guardar")
            else:
                try:
                    # Convertimos los proyectos (listas) a una lista de diccionarios.
                    proyectos_dict = []
                    for p in proyectos:
                        proyectos_dict.append({
                            "nombreProyecto": p[0],
                            "nombreResponsable": p[1],
                            "estado": p[2],
                            "avance": p[3]
                        })
                    
                    # Unimos los proyectos ingresados manualmente con los datos generados aleatoriamente.
                    ambasListas = proyectos_dict + datos
                    
                    # Guardamos el resultado en un archivo JSON con formato legible (indentación).
                    with open("proyecto.json" , "w", encoding="utf-8") as f:
                        json.dump(ambasListas, f, indent=4, ensure_ascii=False)
                        
                    print("Proyecto guardado correctamente")
                except Exception as e:
                    # Si ocurre algún error, lo mostramos por pantalla.
                    print(f"Error al guardar: {e}")
            input("\nPresiona ENTER para continuar...")
        
        
        case "7":
            # === OPCIÓN 7: RECUPERAR PROYECTOS DESDE JSON ===
            # Esta opción lee el archivo 'proyecto.json' y vuelve a cargar los datos en la lista 'proyectos'.
            try:
                with open("proyecto.json", "r", encoding="utf-8") as f:
                    proyectos_dict = json.load(f)
                    
                    # Recorremos todos los elementos del JSON y los agregamos como listas dentro de 'proyectos'.
                    for d in proyectos_dict:
                        proyectos.append([
                            d["nombreProyecto"],
                            d["nombreResponsable"],
                            d["estado"],
                            d["avance"]  # ya viene como número
                        ])
                
                print("Proyecto recuperado correctamente")
                
                # Si después de recuperar no hay datos, se informa.
                if len(proyectos) == 0:
                    print("La agenda está vacía")
                else:
                    # Mostramos todos los proyectos recuperados.
                    for proj in proyectos:
                        # ⚠️ Aquí hay un pequeño error lógico: 'proj' es una lista, no un diccionario.
                        # Por lo tanto, debería accederse con índices (proj[0], proj[1], etc.).
                        nombreProyecto = proj[0]
                        responsable = proj[1]
                        estado = proj[2]
                        avance = proj[3]
                        print(f"\nNombre: {nombreProyecto} - Responsable: {responsable} - Estado: {estado} - Avance: {avance}%")
            
            # Manejo de errores comunes:
            except FileNotFoundError:
                print("No existe un archivo 'proyecto.json'. Guarde primero.")
            except json.JSONDecodeError:
                print("El archivo está dañado o vacío")
            except Exception as e:
                print(f"Error al recuperar: {e}")
            
            input("\nPresiona ENTER para continuar...")
            
            
        case "8":
            # === OPCIÓN 8: GENERAR DATOS ALEATORIOS ===
            # Esta opción genera proyectos falsos automáticamente para hacer pruebas o cargar datos de ejemplo.
            
            entradaDatos = int(input("Ingrese la cantidad de datos que desea generar: "))
            
            # Listas de posibles nombres de proyectos y responsables.
            # Se usarán para seleccionar valores aleatorios.
            nombreProyecto = [            "Sistema de Gestión Escolar", "Plataforma de E-commerce", "App de Reservas Médicas",
            "Gestión de Recursos Humanos", "Control de Inventarios", "Plataforma de Streaming",
            "Sistema de Facturación", "App de Delivery", "Gestión de Proyectos", "CRM Empresarial",
            "Portal de Noticias", "Sistema de Bibliotecas", "App de Transporte Urbano",
            "Red Social Estudiantil", "Sistema de Turnos Online", "Plataforma de Cursos",
            "Control de Producción", "Gestión de Eventos", "App de Finanzas Personales",
            "Sistema de Seguridad", "Plataforma de Viajes", "App de Fitness", "Control de Calidad",
            "Sistema de Hospitales", "Gestión de Almacenes", "App de Compras Locales",
            "Plataforma de Reclutamiento", "Sistema de Reservas Hoteleras", "App de Música",
            "Control de Obras", "Gestión Contable", "Plataforma de Seguros",
            "Sistema de Ventas Minoristas", "App de Transporte Escolar", "Gestión de Clientes",
            "Plataforma de Aprendizaje", "Sistema de Parking", "App de Turismo",
            "Gestión Documental", "Sistema de Soporte Técnico", "App de Bienestar",
            "Plataforma de Donaciones", "Sistema de Votación Online", "App de Mascotas",
            "Gestión de Clínicas", "Sistema de Logística", "App de Idiomas",
            "Control de Stock", "Plataforma de Crowdfunding", "Sistema de Reservas Deportivas",
            "App de Noticias Locales", "Plataforma de Inversiones", "Gestión de Transporte",
            "Sistema de Energía Renovable", "App de Recetas", "Gestión de Hoteles",
            "Plataforma de Podcasts", "Sistema de Bibliotecas Digitales", "App de Agricultura",
            "Gestión de Seguros", "Sistema de Compras Públicas", "App de Fotografía",
            "Plataforma de Voluntariado", "Sistema de Puertos", "App de Salud Mental",
            "Gestión de Escuelas", "Plataforma de Streaming Educativo", "App de Viajes Compartidos",
            "Sistema de Bomberos", "Gestión de Restaurantes", "App de Juegos Educativos",
            "Plataforma de Conferencias", "Sistema de Seguridad Ciudadana", "App de Reciclaje",
            "Gestión de Clubes Deportivos", "Plataforma de Educación Financiera", "App de Transporte Interurbano",
            "Sistema de Bibliotecas Escolares", "Gestión de Universidades", "App de Citas Médicas",
            "Plataforma de Cursos Online", "Sistema de Transporte Marítimo", "App de Deportes",
            "Gestión de Bares", "Plataforma de Streaming Musical", "App de Educación Infantil",
            "Sistema de Aeropuertos", "Gestión de Obras Públicas", "App de Idiomas Infantiles",
            "Plataforma de Networking", "Sistema de Call Center", "App de Radio Online",
            "Gestión de Bancos", "Plataforma de Telemedicina", "App de Reservas Gastronómicas",
            "Sistema de Transporte Aéreo", "Gestión de Hospitales", "App de Podcasts",
            "Plataforma de Crowdsourcing", "Sistema de Archivos Digitales", "App de Bibliotecas Virtuales"
            ]  # Lista larga con nombres de proyectos 
            nombreResponsable = [            "Luciano García", "Martina Fernández", "Juan Pérez", "Sofía Rodríguez", "Diego López",
            "Camila Martínez", "Matías Gómez", "Valentina Díaz", "Julián Torres", "Carolina Romero",
            "Agustín Sosa", "Florencia Álvarez", "Nicolás Ruiz", "Paula Ramírez", "Sebastián Molina",
            "Mariana Castillo", "Gabriel Ortiz", "Laura Silva", "Federico Acosta", "Andrea Medina",
            "Luciano Fernández", "Martina García", "Juan Ramírez", "Sofía López", "Diego Pérez",
            "Camila Torres", "Matías Romero", "Valentina Díaz", "Julián Ortiz", "Carolina Martínez",
            "Agustín Ruiz", "Florencia Sosa", "Nicolás Molina", "Paula García", "Sebastián Fernández",
            "Mariana Ramírez", "Gabriel López", "Laura Pérez", "Federico Romero", "Andrea Torres",
            "Luciano Díaz", "Martina Álvarez", "Juan Castillo", "Sofía Silva", "Diego Ortiz",
            "Camila Medina", "Matías Acosta", "Valentina García", "Julián Fernández", "Carolina Ruiz",
            "Agustín Ramírez", "Florencia López", "Nicolás Pérez", "Paula Romero", "Sebastián Torres",
            "Mariana Díaz", "Gabriel Molina", "Laura Sosa", "Federico Álvarez", "Andrea Castillo",
            "Luciano Silva", "Martina Ortiz", "Juan Medina", "Sofía Acosta", "Diego García",
            "Camila Fernández", "Matías Ramírez", "Valentina López", "Julián Pérez", "Carolina Romero",
            "Agustín Torres", "Florencia Díaz", "Nicolás Molina", "Paula Álvarez", "Sebastián Castillo",
            "Mariana Silva", "Gabriel Ortiz", "Laura Medina", "Federico Acosta", "Andrea García",
            "Luciano Fernández", "Martina López", "Juan Pérez", "Sofía Romero", "Diego Torres",
            "Camila Díaz", "Matías Molina", "Valentina Ramírez", "Julián García", "Carolina Fernández",
            "Agustín Ortiz", "Florencia Silva", "Nicolás Medina", "Paula Acosta", "Sebastián Romero",
            "Mariana López", "Gabriel Torres", "Laura Castillo", "Federico Pérez", "Andrea Molina"
            ]  # Lista con nombres de responsables 
            
            # Se generan tantos proyectos como el usuario haya indicado.
            for _ in range(entradaDatos):
                # Seleccionamos un estado aleatorio entre los estados válidos (por ejemplo: "En progreso", "Finalizado"...)
                estadoAleatorio = random.randint(1,3)
                estadoAleatorio = estados_validos[estadoAleatorio]
                
                # Creamos un diccionario con los datos generados y lo agregamos a la lista 'datos'.
                datos.append({
                    "nombreProyecto": random.choice(nombreProyecto),
                    "nombreResponsable": random.choice(nombreResponsable),
                    "estado": estadoAleatorio,
                    "avance": random.randint(1,100)
                })
            
            print(f"La cantidad de {entradaDatos} datos aleatorios generados correctamente")
            
            # Mostramos en pantalla todos los datos generados.
            for item in datos:
                print(item)
                
            input("\nPresiona ENTER para continuar...")                
                
            # Creamos un DataFrame con los datos usando pandas.
            df = pd.DataFrame(datos)
            
            # Guardamos esos datos aleatorios en un archivo 'datos_random.json' para tener respaldo.
            df.to_json(f"datos_random.json", orient="records", indent=4)

            
        case "9":
            # ========================
            # Función de carga visual (animación)
            # ========================
            def loading(msg="Generando gráfico"):
                """Muestra una animación de carga con puntos y un mensaje."""
                print(Fore.YELLOW + msg, end="")  # Imprime el mensaje sin salto de línea
                for _ in range(3):                # Hace tres puntos de espera
                    time.sleep(0.5)               # Espera medio segundo entre puntos
                    print(".", end="")
                    sys.stdout.flush()            # Fuerza la actualización inmediata en consola
                print(" ✅" + Style.RESET_ALL)     # Muestra un check verde al final
            
            # ========================
            # Carga y preparación de los datos
            # ========================
            data = pd.read_json("proyecto.json")   # Carga los datos desde un archivo JSON
            df = pd.DataFrame(data)                # Convierte los datos en un DataFrame de pandas
            
            # ========================
            # Funciones de gráficos individuales
            # ========================

            def grafico_barras(df, mostrar=True):
                """Gráfico de barras con el avance de cada proyecto."""
                plt.figure(figsize=(10, 6))  # Define tamaño del gráfico
                sns.barplot(x='nombreProyecto', y='avance', data=df, palette='coolwarm')  # Crea el gráfico de barras
                plt.title('Avance de cada Proyecto', fontsize=16, fontweight='bold')      # Título principal
                plt.xlabel('Proyecto')
                plt.ylabel('Porcentaje de avance')
                plt.xticks(rotation=90, ha='right')  # Rota etiquetas del eje X
                plt.ylim(0, 100)                     # Límite del eje Y entre 0 y 100
                plt.tight_layout()                   # Ajusta espacios para que no se solapen
                if mostrar:
                    plt.show()                       # Muestra el gráfico si se indica

            def grafico_conteo_estado(df, mostrar=True):
                """Cantidad de proyectos por estado."""
                plt.figure(figsize=(10, 6))
                sns.countplot(x='estado', data=df, palette='Set2')  # Muestra la cantidad de proyectos por cada estado
                plt.title('Cantidad de Proyectos por Estado', fontsize=16, fontweight='bold')
                plt.xlabel('Estado')
                plt.ylabel('Cantidad')
                plt.tight_layout()
                if mostrar:
                    plt.show()

            def grafico_dispersion(df, mostrar=True):
                """Relación entre proyectos y su avance."""
                plt.figure(figsize=(10, 6))
                # Gráfico de dispersión donde cada punto representa un proyecto
                sns.scatterplot(x='nombreProyecto', y='avance', hue='estado', data=df, s=200)
                plt.title('Relación entre Proyectos y Avance', fontsize=16, fontweight='bold')
                plt.xlabel('Proyecto')
                plt.ylabel('Avance (%)')
                plt.xticks(rotation=90, ha='right')
                plt.ylim(0, 100)
                plt.legend(title='Estado')  # Muestra una leyenda con los estados
                plt.tight_layout()
                if mostrar:
                    plt.show()

            def grafico_torta(df, mostrar=True):
                """Proporción de proyectos por estado."""
                plt.figure(figsize=(8, 8))
                conteo = df['estado'].value_counts()  # Cuenta cuántos proyectos hay por estado
                plt.pie(
                    conteo,
                    labels=conteo.index,              # Etiquetas: nombres de los estados
                    autopct='%1.1f%%',                # Muestra el porcentaje con un decimal
                    startangle=140,                   # Rota el inicio del gráfico para mejor visualización
                    colors=sns.color_palette('Set2')  # Usa una paleta de colores amigable
                )
                plt.title('Proporción de Proyectos por Estado', fontsize=16, fontweight='bold')
                plt.tight_layout()
                if mostrar:
                    plt.show()

            def grafico_general(df, mostrar=True):
                """Muestra los 4 gráficos en una figura combinada."""
                # Crea una figura con 4 subgráficos (2 filas x 2 columnas)
                fig, axs = plt.subplots(2, 2, figsize=(18, 10))
            
                # --- Gráfico de barras ---
                sns.barplot(x='nombreProyecto', y='avance', data=df, palette='coolwarm', ax=axs[0, 0])
                axs[0, 0].set_title("Avance de cada Proyecto")
                axs[0, 0].tick_params(axis='x', rotation=90)
            
                # --- Gráfico de conteo ---
                sns.countplot(x='estado', data=df, palette='Set2', ax=axs[0, 1])
                axs[0, 1].set_title("Cantidad de Proyectos por Estado")
            
                # --- Gráfico de dispersión ---
                sns.scatterplot(x='nombreProyecto', y='avance', hue='estado', data=df, s=150, ax=axs[1, 0])
                axs[1, 0].set_title("Relación entre Proyecto y Avance")
                axs[1, 0].tick_params(axis='x', rotation=90)
            
                # --- Gráfico de torta ---
                conteo = df['estado'].value_counts()
                axs[1, 1].pie(conteo, labels=conteo.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('Set2'))
                axs[1, 1].set_title("Proporción de Proyectos por Estado")
            
                plt.tight_layout()  # Ajusta la separación entre los gráficos
                if mostrar:
                    plt.show()       # Muestra todos juntos
                return fig           # Devuelve la figura (por si se necesita guardar)

            # =============================
            # 📑 Generación del PDF con gráficos
            # =============================
            def generar_pdf(df, carpeta):
                """Crea un PDF con los gráficos y un resumen de los proyectos."""
                
                # --- Ruta de destino del PDF ---
                pdf_path = os.path.join(carpeta, "reporte_graficos.pdf")  # Guarda el archivo dentro de la carpeta indicada
                doc = SimpleDocTemplate(pdf_path, pagesize=A4)             # Define formato A4 del documento
                estilos = getSampleStyleSheet()                            # Usa estilos predefinidos
                contenido = []                                             # Lista donde se irán agregando los elementos del PDF
            
                # --- Título principal ---
                contenido.append(Paragraph("<b>Reporte de Proyectos</b>", estilos["Title"]))  # Agrega título
                contenido.append(Spacer(1, 20))  # Espacio entre título y contenido
            
                # --- Resumen de los datos ---
                resumen = f"""
                <b>Total de proyectos:</b> {len(df)}<br/>
                <b>Promedio de avance:</b> {df['avance'].mean():.2f}%<br/>
                <b>Estados presentes:</b> {', '.join(df['estado'].unique())}
                """
                contenido.append(Paragraph(resumen, estilos["Normal"]))  # Inserta resumen como párrafo
                contenido.append(Spacer(1, 20))
            
                # --- Tabla de proyectos ---
                data_tabla = [["Proyecto", "Responsable", "Estado", "Avance (%)"]]  # Encabezados
                for _, row in df.iterrows():  # Itera sobre cada fila del DataFrame
                    data_tabla.append([row["nombreProyecto"], row["nombreResponsable"], row["estado"], row["avance"]])
            
                tabla = Table(data_tabla, colWidths=[120, 120, 100, 80])  # Define ancho de las columnas
                tabla.setStyle(TableStyle([
                    ("BACKGROUND", (0, 0), (-1, 0), colors.lightblue),     # Fondo azul en encabezado
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),     # Texto blanco
                    ("ALIGN", (0, 0), (-1, -1), "CENTER"),                 # Centra texto en toda la tabla
                    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),          # Bordes grises
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),       # Negrita para encabezado
                ]))
                contenido.append(tabla)
                contenido.append(Spacer(1, 30))
            
                # --- Inserción de gráficos en el PDF ---
                graficos = [
                    ("Avance de Proyectos", "grafico_barras.png"),
                    ("Cantidad por Estado", "grafico_conteo_estado.png"),
                    ("Relación Proyecto vs Avance", "grafico_dispersion.png"),
                    ("Proporción por Estado", "grafico_torta.png"),
                    ("Vista General", "todos_graficos.png"),
                ]
            
                # Recorre los archivos de gráficos guardados y los agrega si existen
                for titulo, archivo in graficos:
                    img_path = os.path.join(carpeta, archivo)
                    if os.path.exists(img_path):  # Verifica que la imagen exista antes de insertarla
                        contenido.append(Paragraph(f"<b>{titulo}</b>", estilos["Heading2"]))
                        contenido.append(Spacer(1, 10))
                        contenido.append(Image(img_path, width=450, height=280))  # Inserta la imagen con tamaño fijo
                        contenido.append(Spacer(1, 20))
            
                # --- Construcción final del documento PDF ---
                doc.build(contenido)  # Genera el PDF con todos los elementos
                print("📄 PDF generado:", pdf_path)  # Muestra en consola la ubicación del archivo

            
            # =============================
            # 🌐 HTML
            # =============================
            
            def generar_html_interactivo(carpeta):
                """Crea un HTML interactivo con un selector de gráficos."""
                html = """<!DOCTYPE html>
            <html lang="es">
            <head>
                <meta charset="UTF-8">
                <title>Reporte de Gráficos</title>
                <style>
                    body { font-family: Arial, sans-serif; background: #f5f6fa; text-align: center; margin: 40px; }
                    h1 { color: #2f3640; }
                    select { padding: 10px; font-size: 16px; border-radius: 10px; border: 1px solid #ccc; margin: 20px; }
                    img { width: 80%%; max-width: 900px; margin-top: 30px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.2); }
                </style>
            </head>
            <body>
                <h1>Reporte de Gráficos de Proyectos</h1>
                <select id="graficoSelector">
                    <option value="grafico_barras.png">Avance de Proyectos (Barras)</option>
                    <option value="grafico_conteo_estado.png">Cantidad por Estado</option>
                    <option value="grafico_dispersion.png">Relación Proyecto vs Avance</option>
                    <option value="grafico_torta.png">Proporción por Estado (Torta)</option>
                    <option value="todos_graficos.png">Todos los Gráficos</option>
                </select>
                <div>
                    <img id="imagenGrafico" src="grafico_barras.png" alt="Gráfico actual">
                </div>
                <script>
                    const selector = document.getElementById('graficoSelector');
                    const imagen = document.getElementById('imagenGrafico');
                    selector.addEventListener('change', () => { imagen.src = selector.value; });
                </script>
            </body>
            </html>
            """
                # ============================================
                # 💾 Generación del archivo HTML con gráficos
                # ============================================
                with open(os.path.join(carpeta, "reporte_graficos.html"), "w", encoding="utf-8") as f:
                    f.write(html)  # Escribe el contenido HTML en el archivo
                print("🌐 HTML generado:", os.path.join(carpeta, "reporte_graficos.html"))  # Confirma creación del HTML
            
            # =============================
            # 🧾 GENERAR REPORTES COMPLETOS
            # =============================
            def generar_reportes(df):
                """Genera los reportes en diferentes formatos (PDF y HTML) y guarda los gráficos."""
                
                carpeta = "reportes"  # Carpeta donde se guardarán todos los reportes
                os.makedirs(carpeta, exist_ok=True)  # Crea la carpeta si no existe
            
                print("📊 Generando reportes...")
            
                plt.close('all')  # Cierra cualquier gráfico abierto previamente para evitar superposición
            
                # ============================
                # 🔹 Guardar gráficos individuales (sin mostrarlos)
                # ============================

                # Gráfico de barras
                grafico_barras(df, mostrar=False)  # Genera el gráfico pero no lo muestra en pantalla
                plt.savefig(os.path.join(carpeta, "grafico_barras.png"), bbox_inches="tight")  # Lo guarda como imagen PNG
                plt.close()  # Cierra la figura para liberar memoria
            
                # Gráfico de conteo por estado
                grafico_conteo_estado(df, mostrar=False)
                plt.savefig(os.path.join(carpeta, "grafico_conteo_estado.png"), bbox_inches="tight")
                plt.close()
            
                # Gráfico de dispersión
                grafico_dispersion(df, mostrar=False)
                plt.savefig(os.path.join(carpeta, "grafico_dispersion.png"), bbox_inches="tight")
                plt.close()
            
                # Gráfico de torta
                grafico_torta(df, mostrar=False)
                plt.savefig(os.path.join(carpeta, "grafico_torta.png"), bbox_inches="tight")
                plt.close()
            
                # Gráfico general con los 4 combinados
                fig = grafico_general(df, mostrar=False)  # Devuelve una figura con subgráficos
                fig.savefig(os.path.join(carpeta, "todos_graficos.png"), bbox_inches="tight")  # Se guarda como imagen
                plt.close(fig)  # Cierra la figura completa
            
                # ============================
                # 🔹 Generar PDF y HTML
                # ============================
                generar_pdf(df, carpeta)                # Crea el reporte en formato PDF
                generar_html_interactivo(carpeta)       # Crea el reporte interactivo en formato HTML
            
                # ============================
                # 🔹 Mensaje final de confirmación
                # ============================
                print("✅ Reporte generado exitosamente en la carpeta 'reportes'")
            
            # ============================================
            # 🎨 MENÚ DE OPCIONES DE GRÁFICOS INTERACTIVOS
            # ============================================
            while True:
                # Muestra el título del menú con color cian
                print(Fore.CYAN + "\n============================")
                print("   MENÚ DE GRÁFICOS")
                print("============================" + Style.RESET_ALL)
        
                # Opciones disponibles
                print("1. Gráfico de Líneas")       # (en realidad muestra el de barras, pero mantiene este nombre)
                print("2. Gráfico de Histogama")   # Muestra la relación entre avance y estado
                print("3. Gráfico de Dispersión")              # Opción que se asocia al gráfico de dispersión
                print("4. Gráfico de Torta")       # Proporción de proyectos (gráfico de torta)
                print("5. Mostrar todos los gráficos")
                print("6. Generar reporte")
                print("0. Salir")
        
                # Solicita al usuario elegir una opción
                opcion = input(Fore.GREEN + "\n👉 Elige una opción: " + Style.RESET_ALL)
        
                # Dependiendo de la opción elegida, se ejecuta una función
                if opcion == "1":
                    grafico_barras(df)              # Muestra gráfico de barras
                elif opcion == "2":
                    grafico_conteo_estado(df)       # Muestra gráfico de conteo por estado
                elif opcion == "3":
                    grafico_dispersion(df)          # Muestra gráfico de dispersión
                elif opcion == "4":
                    grafico_torta(df)               # Muestra gráfico de torta
                elif opcion == "5":
                    grafico_general(df)             # Muestra todos los gráficos juntos
                elif opcion == "6":
                    generar_reportes(df)            # Genera todos los reportes (PDF + HTML)
                elif opcion == "0":
                    # break corta el bucle y sale del menú
                    #print("Saliendo... 👋")
                    break
                else:
                    # Si el usuario elige una opción que no existe
                    print(Fore.RED + "⚠️ Opción no válida, intenta de nuevo.")
        case "10":
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
