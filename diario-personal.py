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

#Funcion para crear Diario:
def crear_Diario():
    limpiar_consola() #Limpiamos la Consola antes de crear un nuevo Diario
    print("➕  **Crear Nueva Diario del Diario** ➕")  
    fecha = input("Fecha (DD-MM-AAAA): ")  # Solicitamos la fecha
    titulo = input("Título: ")             # Solicitamos el título
    entrada = input("Entrada: ")           # Solicitamos el contenido  
    diario.append([fecha, titulo,entrada]) # Agregamos el contenido en la lista
    print("\n✅ ¡Diario guardada exitosamente! ✅")
    pausar()  # Pausamos para que el usuario vea el mensaje

#Funcion para Ver el Diario:
def ver_Diarios(pausar_despues=True):
    limpiar_consola()  # Limpiamos la pantalla
    print("\033[96m" + "═" * 45 + "\033[0m")
    print("📖  \033[1mTus Diarios\033[0m")
    print("\033[96m" + "═" * 45 + "\033[0m")
    
    if not diario:
        print("\n😔 Aún no tienes Diarios en tu diario. ¡Añade una nueva! 😔")
    else:
        # Recorremos la lista con enumerate para mostrar índice y datos
        for i,(fecha, titulo, entrada) in enumerate(diario,start=1):
            print(f"\n\033[93mEntrada #{i}\033[0m")
            print(f"🗓  Fecha : \033[92m{fecha}\033[0m")
            print(f"📌 Título: \033[94m{titulo}\033[0m")
            print("📜 Texto :")
            print(f"    {entrada}")
            print("\033[96m" + "-" * 45 + "\033[0m")
    if pausar_despues:  # Pausamos solo si el parámetro lo indica
        pausar()        

#Funcion para seleccionar numero de Diario:
def Seleccionar_Diario():
    if not diario:  # Si la lista está vacía
        print("\n😔 No hay Diarios disponibles. 😔")
        pausar()
        return None

    # Mostramos los diarios sin pausar
    ver_Diarios(pausar_despues=False)

    try:
        # Solicitamos número de Diario
        num = int(input("\nIngresa el número del Diario: ")) - 1  

        # Validamos que el índice esté dentro del rango
        if 0 <= num < len(diario):
            return num
        else:
            print("❌ Número de Diario no válido. ❌")
            pausar()
            return None

    except ValueError:
        # Si no se ingresa un número entero
        print("❌ Entrada inválida. Por favor, ingresa un número. ❌")
        pausar()
        return None
    
#Funcion para actualizar el contenido de un Diario:
def actualizar_Diario():
    print("\033[96m" + "═" * 45 + "\033[0m")
    print(" ✏️ \033[1mActualizar Diario Existente\033[0m")
    print("\033[96m" + "═" * 45 + "\033[0m")
    index= Seleccionar_Diario() #Obtenemos el indice del diario
    if index is None:
        return
    diario_act = diario[index]   #Obtenemos el diario 
    
    #Lo mostramos en la consola:
    print("\n\033[93m📖 Diario Seleccionado:\033[0m")
    print("\033[92m🗓  Fecha :\033[0m", diario_act[0])
    print("\033[94m📌 Título:\033[0m", diario_act[1])
    print("\033[97m📝 Texto :\033[0m")
    print("   " + diario_act[2])
    print("\033[96m" + "─" * 45 + "\033[0m")
    
    # Pedimos nuevos datos; si el usuario deja vacío, se mantiene el original
    nueva_fecha = input(f"Nueva Fecha ({diario_act[0]}): ") or diario_act[0]
    nuevo_titulo = input(f"Nuevo Título ({diario_act[1]}): ") or diario_act[1]
    nueva_Entrada = input(f"Nueva Diario ({diario_act[2]}): ") or diario_act[2]
    
    #Actualizamos el nuevo diario:
    diario[index]=[nueva_fecha, nuevo_titulo, nueva_Entrada]
    print("\n✅ ¡Diario actualizada exitosamente! ✅")
    pausar()  # Pausamos para que el usuario vea el mensaje
    
#Funcion para Eiminar un Diario
def eliminar_Diario():
    print("\033[96m" + "═" * 45 + "\033[0m")
    print(" 🗑️ \033[1mEliminar Diario\033[0m")
    print("\033[96m" + "═" * 45 + "\033[0m")
    index =Seleccionar_Diario()# Obtenemos el indice del diario a eliminar
    if index is None:
        return    
    
    Diario_eliminada = diario.pop(index)  # Eliminamos la Diario de la lista
    print(f"\n✅ Diario '{Diario_eliminada[1]}' eliminada exitosamente. ✅")
    pausar()  # Pausamos para que el usuario vea el mensaje
    
#Funcion para Buscar un diario por su Titulo:
def buscar_Diario_PorTitulo():
    limpiar_consola()
    print("\033[96m" + "═" * 45 + "\033[0m")
    print(" 🔍 \033[1mBuscar Diario por Titulo🔍\033[0m")
    print("\033[96m" + "═" * 45 + "\033[0m")   
    
    if not diario:  # Si no hay Diarios, avisamos
        print("\n😔 No hay Diarios para buscar. 😔")
        pausar()
        return
    titulo_buscado = input("Ingrese el titulo o parte del titulo a buscar:").lower()
    encontrados = [e for e in diario if titulo_buscado in e[1].lower()]  # Buscamos coincidencias
    if encontrados:
        print("\n✨ Diarios encontradas: ✨")
        for i, Diario in enumerate(encontrados, start=1):
            print(f"\nDiario #{i} | Fecha: {Diario[0]} | Título: {Diario[1]} | Diario: {Diario[2]}")
    else:
        print("\n😔 No se encontraron Diarios con ese criterio. 😔")
    pausar()  # Pausamos para que el usuario vea los resultados

def guardar_Diario():
    #Guarda la lista global 'diario' en un archivo CSV."""
    limpiar_consola() #Limpiamos primero la consola
    
    print("\033[96m" + "═" * 50 + "\033[0m")
    print(" 💾 \033[1mGuardar Diario en archivo CSV\033[0m 💾")
    print("\033[96m" + "═" * 50 + "\033[0m")

    if not diario:
        print("\n😔 No hay entradas para guardar. 😔")
        pausar()
        return

    try:
        nombre_archivo = "diario.csv"
        with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerows(diario)  # Guarda cada entrada como fila
        print(f"\n✅ Diario guardado correctamente en '{nombre_archivo}' ✅")
    except Exception as e:
        print(f"❌ Error al guardar el diario: {e} ❌")

    pausar()


# ──────────────────────────────────────────────
# Función para cargar el diario desde archivo CSV
# ──────────────────────────────────────────────
def cargar_diario_csv():
    #Carga las entradas de 'diario.csv' en la lista global 'diario'.
    limpiar_consola() #Limpiamos primero la consola
    print("\033[96m" + "═" * 50 + "\033[0m")
    print(" 📂 \033[1mCargar Diario desde archivo CSV\033[0m 📂")
    print("\033[96m" + "═" * 50 + "\033[0m")

    try:
        nombre_archivo = "diario.csv"
        with open(nombre_archivo, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            diario.clear()              # Limpia la lista actual
            diario.extend(list(lector)) # Añade todas las filas leídas
            
            if diario:  # ✅ Solo mostramos si hay datos
                print(f"\n✅ Diario cargado desde '{nombre_archivo}' ✅")
                print("\n📖 Entradas recuperadas:\n")
                ver_Diarios(pausar_despues=False)   # 👈 Muestra en pantalla
            else:
                print("\n⚠️ El archivo estaba vacío.")
                
    except FileNotFoundError:
        print("❌ No se encontró el archivo 'diario.csv'. ❌")
    except Exception as e:
        print(f"❌ Error al cargar el diario: {e} ❌")

    pausar()  
# =====================================
# Función principal que controla el flujo del programa
# =====================================
def main():
    """
    Controla el menú y mantiene el programa activo hasta que el usuario decida salir.
    """
    while True:  # Bucle infinito hasta que se elija salir
        mostrar_menu()  # Mostramos el menú
        opcion = input("Elige una opción: ")  # Solicitamos opción al usuario
        
        # Aquí se llaman las funciones correspondientes según la opción
    # Usando match/case para controlar opciones
        match opcion:
            case '1':
                crear_Diario()
            case '2':
                ver_Diarios()
            case '3':
                actualizar_Diario()
            case '4':
                eliminar_Diario()
            case '5':
                buscar_Diario_PorTitulo()
            case '6':
                guardar_Diario()
            case '7':
                cargar_diario_csv()
            case '8':  # Salir
                print("¡Hasta luego! 👋")
                break
            case _:  # Caso por defecto si no coincide ninguna opción
                print("Opción inválida, intenta nuevamente.")
                input("Presiona Enter para continuar...")



# Bloque principal que ejecuta el menú si este archivo se corre directamente
if __name__ == "__main__":
    main()    