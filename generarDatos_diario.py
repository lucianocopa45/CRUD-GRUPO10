# Importamos librerías necesarias
import os      # Para limpiar la consola según el sistema operativo
import json     # Para leer y escribir archivos json
import time    #Para pausar la ejecucion 
import pandas as pd #Para analizar y mostrar los datos en formato de tablas
import random #Para seleccionar datoss aleatorios
from datetime import datetime, timedelta #Para generar Fechas aleatorias en los ultimos 365 dias
import matplotlib.pyplot as matp #Matplolib: crea los graficos
import seaborn as sb #seaborn: Crea graficos estadisticos mas esteticos que Matplotlib
import calendar  #Para obtener nombre y numeros de los meses del año



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
    print("║")  # Cierra la línea del recuadro del título
    print(CYAN + "╚" + "═" * 40 + "╝" + RESET)  # Parte inferior del recuadro del título

    # Lista de opciones del menú con colores y emojis
    opciones = [
        (GREEN, "1. ➕ Crear Diario"),
        (CYAN, "2. 📖 Ver Diarios"),
        (YELLOW, "3. ✏️ Actualizar Diario"),
        (MAGENTA, "4. 🗑️ Eliminar Diario"),
        (GREEN, "5. 🔍 Buscar Diario"),
        (CYAN, "6. 💾 Guardar Diario (JSON)"),
        (YELLOW, "7. 📂 Cargar Diario (JSON)"),
        (MAGENTA, "8. 📝 Generar Datos aleatorios(JSON)"),
        (GREEN, "9. 📊 Generar Graficos"),
        (CYAN, "10. 🚪 Salir")
    ]
    

    # Separador animado superior del menú
    separador = "─" * 40  # Creamos una línea de 40 caracteres
    for char in separador:
        print(CYAN + char + RESET, end="", flush=True)  # Imprime cada guion con color cian
        time.sleep(0.02)  # Pausa muy breve para efecto animado
    print()  # Salto de línea al finalizar el separador

    # Imprimimos cada opción del menú con un pequeño retraso para efecto visual
    for color, opcion in opciones:
        print(color + opcion + RESET)  # Imprime la opción con su color correspondiente
        time.sleep(0.02)  # Pequeña pausa para efecto animación

    # Separador animado inferior del menú
    for char in separador:
        print(CYAN + char + RESET, end="", flush=True)  # Imprime cada guion con color cian
        time.sleep(0.02)  # Pausa breve
    print()  # Salto de línea al finalizar el separador

#Funcion para crear Diario:
def crear_Diario():
    limpiar_consola()  # Limpiamos la Consola antes de crear un nuevo Diario
    print("➕  **Crear Nueva Entrada del Diario** ➕")  
    fecha = input("Fecha (DD-MM-AAAA): ")  # Solicitamos la fecha
    titulo = input("Título: ")             # Solicitamos el título
    entrada = input("Entrada: ")           # Solicitamos el contenido  
    
    # Guardamos como diccionario
    nueva_entrada = {
        "fecha": fecha,
        "titulo": titulo,
        "entrada": entrada
    }

    diario.append(nueva_entrada)  # Agregamos el contenido en la lista
    print("\n✅ ¡Diario guardado exitosamente! ✅")
    pausar()  # Pausamos para que el usuario vea el mensaje


#Funcion para Ver el Diario:
def ver_Diarios(pausar_despues=True):
    limpiar_consola()  # Limpiamos la pantalla
    print("\033[96m" + "═" * 45 + "\033[0m")
    print("📖  \033[1mTus Diarios\033[0m")
    print("\033[96m" + "═" * 45 + "\033[0m")
    
    
    if not diario:
            try:
                cargar_diario_json()
            except FileNotFoundError:
                pass  # Si no existe el archivo, se ignora
            
    if not diario:
        print("\n😔 Aún no tienes Diarios en tu diario. ¡Añade una nueva! 😔")
    else: # Si hay entradas, se recorren y muestran con formato estético
        for i, entrada in enumerate(diario, start=1):
            print(f"\n\033[93mEntrada #{i}\033[0m")
            print(f"🗓  Fecha : \033[92m{entrada['fecha']}\033[0m")
            print(f"📌 Título: \033[94m{entrada['titulo']}\033[0m")
            print("📜 Texto :")
            print(f"    {entrada['entrada']}")
            print("\033[96m" + "-" * 45 + "\033[0m")
    
    if pausar_despues:
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
    

# Funcion para actualizar el contenido de un Diario:
def actualizar_Diario():
    print("\033[96m" + "═" * 45 + "\033[0m")
    print(" ✏️ \033[1mActualizar Diario Existente\033[0m")
    print("\033[96m" + "═" * 45 + "\033[0m")
    index = Seleccionar_Diario()  # Obtenemos el índice del diario
    if index is None:
        return
    diario_act = diario[index]   # Obtenemos el diario (diccionario)
    
    # Lo mostramos en la consola:
    print("\n\033[93m📖 Diario Seleccionado:\033[0m")
    print("\033[92m🗓  Fecha :\033[0m", diario_act["fecha"])
    print("\033[94m📌 Título:\033[0m", diario_act["titulo"])
    print("\033[97m📝 Texto :\033[0m")
    print("   " + diario_act["entrada"])
    print("\033[96m" + "─" * 45 + "\033[0m")
    
    # Pedimos nuevos datos; si el usuario deja vacío, se mantiene el original
    nueva_fecha = input(f"Nueva Fecha ({diario_act['fecha']}): ") or diario_act["fecha"]
    nuevo_titulo = input(f"Nuevo Título ({diario_act['titulo']}): ") or diario_act["titulo"]
    nueva_entrada = input(f"Nueva Entrada ({diario_act['entrada']}): ") or diario_act["entrada"]
    
    # Actualizamos el diario (modificando el diccionario directamente)
    diario[index] = {
        "fecha": nueva_fecha,
        "titulo": nuevo_titulo,
        "entrada": nueva_entrada
    }
    
    print("\n✅ ¡Diario actualizado exitosamente! ✅")
    pausar()  # Pausamos para que el usuario vea el mensaje


# Funcion para Eliminar un Diario
def eliminar_Diario():
    print("\033[96m" + "═" * 45 + "\033[0m")
    print(" 🗑️ \033[1mEliminar Diario\033[0m")
    print("\033[96m" + "═" * 45 + "\033[0m")
    index = Seleccionar_Diario()  # Obtenemos el índice del diario a eliminar
    if index is None:
        return    
    
    diario_eliminado = diario.pop(index)  # Eliminamos el diario (diccionario)
    print(f"\n✅ Diario '{diario_eliminado['titulo']}' eliminado exitosamente. ✅")
    pausar()  # Pausamos para que el usuario vea el mensaje

    
def salir():
       print("\033[96m" + "═" * 45 + "\033[0m")
       print(" 👋 \033[1m¡Hasta luego!\033[0m")
       print("\033[96m" + "═" * 45 + "\033[0m")

    
#Funcion para Buscar un diario por su Titulo:
def buscar_Diario_PorTitulo():
    limpiar_consola()
    print("\033[96m" + "═" * 45 + "\033[0m")
    print(" 🔍 \033[1mBuscar Diario por Título🔍\033[0m")
    print("\033[96m" + "═" * 45 + "\033[0m")

    # Si el diario está vacío, no hay nada que buscar
    if not diario:
        print("\n😔 No hay entradas en el diario para buscar. 😔")
        pausar()
        return

    # Solicitar el texto a buscar (no sensible a mayúsculas)
    titulo_buscado = input("Ingrese el título o parte del título a buscar: ").lower()

    # Buscar coincidencias parciales en los títulos
    encontrados = [
        entrada for entrada in diario
        if titulo_buscado in entrada["titulo"].lower()
    ]

    # Mostrar resultados
    if encontrados:
        print("\n✨ Entradas encontradas: ✨")
        for i, entrada in enumerate(encontrados, start=1):
            print(f"\nEntrada #{i}")
            print(f"🗓  Fecha : {entrada['fecha']}")
            print(f"📌 Título: {entrada['titulo']}")
            print("📜 Texto :")
            print(f"    {entrada['entrada']}")
            print("\033[96m" + "-" * 45 + "\033[0m")
    else:
        print("\n😔 No se encontraron entradas con ese criterio. 😔")

    pausar()
def guardar_Diario():
    #Guarda la lista global 'diario' en un archivo JSON.
    limpiar_consola() #Limpiamos primero la consola
    
    print("\033[96m" + "═" * 50 + "\033[0m")
    print(" 💾 \033[1mGuardar Diario en archivo CSV\033[0m 💾")
    print("\033[96m" + "═" * 50 + "\033[0m")

    if not diario:
        print("\n😔 No hay entradas para guardar. 😔")# Verificar si hay entradas en el diario
        pausar()
        return
    
        # Guardar el diario en archivo JSON
    try:
        nombre_archivo = "diario.json"
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(diario, archivo, ensure_ascii=False, indent=4)  # 👈 Guardar con formato bonito
        print(f"\n✅ Diario guardado correctamente en '{nombre_archivo}' ✅")
    except Exception as e:
        print(f"❌ Error al guardar el diario: {e} ❌")

    pausar() # Pausar para que el usuario vea el mensaje

# ──────────────────────────────────────────────
# Función para cargar el diario desde archivo JSON
# ──────────────────────────────────────────────
def cargar_diario_json():
    limpiar_consola()
    print("\033[96m" + "═" * 50 + "\033[0m")# Imprime una línea decorativa de 50 caracteres en color cyan para separar visualmente el encabezado.
    print(" 📂 \033[1mCargar Diario desde archivo JSON\033[0m 📂")
    print("\033[96m" + "═" * 50 + "\033[0m")

    try:
        nombre_archivo = "diario.json" # Define el nombre del archivo JSON de donde se cargarán los datos.
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:  #Abre el archivo en modo lectura ('r') con codificación UTF-8 para soportar caracteres especiales.
            datos = json.load(archivo)   # Leer JSON
            diario.clear()# Vacía la lista global `diario` para reemplazar su contenido con los datos cargados Y no duplicar datos..
            diario.extend(datos)

            if diario:
                print(f"\n✅ Diario cargado desde '{nombre_archivo}' ✅")
                # Mostrar las entradas cargadas
                ver_Diarios(pausar_despues=False)
            else:
                print("\n⚠️ El archivo estaba vacío.")
    except FileNotFoundError:
        print("❌ No se encontró el archivo 'diario.json'. ❌")
    except Exception as e:
        print(f"❌ Error al cargar el diario: {e} ❌")

    pausar()  # Pausa para que el usuario vea todo
    
    
#===========================================
#Funcion para Generar Datos aleatoriamente
#===========================================

# Lista global
diario = []

# Ejemplos de títulos y entradas
titulos_ejemplos = ["Un dia inolvidable", "Reflexiones", "Momentos felices",
                    "Pensamientos", "Una aventura", "Lindo encuentro", "Recuerdos", "Sueños"]

entradas_ejemplos = [
    "Hoy fue un dia inolvidable porque...", "Me senti inspirada al ver...", "Hoy aprendi algo nuevo...",
    "Pase tiempo con amigos y fue genial...", "Recorde un grato momento de mi infancia...",
    "Me senti agradecida porque...", "Tuve un lindo sueño sobre...", "Hoy me encontre con una ex compañera del colegio"
]

# Función para generar fechas aleatorias
def generar_fechas_aleatorias(cantidad):
    hoy = datetime.today()
    return [(hoy - timedelta(days=random.randint(0, 365))).strftime("%d-%m-%Y") for _ in range(cantidad)] #Elige una fecha aleatoria desde hoy hasta 365 dias atras

# Función para generar datos aleatorios y guardarlos
def GenerarDatos_aleatorio():
    global diario  # usamos la lista global
    
    #  Cargar datos existentes del JSON, si existe
    try:
        df_existente = pd.read_json("diario.json") # Intenta leer el archivo 'diario.json' usando pandas y cargarlo como DataFrame.
        diario = df_existente.to_dict(orient="records") # Convierte el DataFrame a una lista de diccionarios para manipularlo fácilmente en Python.

    except FileNotFoundError:
        diario = []  # Si no existe el archivo, empezamos con lista vacía
    
    try:
        cantidad = int(input("Ingrese la cantidad de datos a generar: ")) # Solicita al usuario la cantidad de entradas aleatorias que desea generar.
    except ValueError:
        print("❌ Entrada inválida. Debe ingresar un número entero.")
        return  # sale de la función si hay error

    # Generar datos aleatorios
    fechas = generar_fechas_aleatorias(cantidad) # Llama a la función que genera fechas aleatorias según la cantidad solicitada.
    titulos = [random.choice(titulos_ejemplos) for _ in range(cantidad)]  #Genera una lista de títulos aleatorios seleccionados de la lista `titulos_ejemplos`.
    entradas = [random.choice(entradas_ejemplos) for _ in range(cantidad)] # Genera una lista de textos de entrada aleatorios seleccionados de `entradas_ejemplos`.

    # Crear lista de diccionarios
    nuevas_entradas = [{"fecha": fechas[i], "titulo": titulos[i], "entrada": entradas[i]} for i in range(cantidad)]

    # Agregar a la lista global
    diario.extend(nuevas_entradas)

    # Guardar todo en JSON usando pandas
    df = pd.DataFrame(diario)
    df.to_json("diario.json", orient="records", indent=4, force_ascii=False)

    print(f"\n✅ Se generaron {cantidad} entradas aleatorias y se guardaron en 'diario.json' ✅")
    pausar()

#=====================================
# Funcion Generar Graficos y reportes
#=====================================
"""PROMPT CHATGTP:
Necesito crear 4 graficos y mostrarlos en un 5to grafico todos juntos.Para la generacion de cada tipo de grafico, hacer una funcion. Puede ser de linea, de barras, histograma y de torta.
Para una mayor visualizacion y analisis de los mismos, necesito que se muestre, titulo general, etiquetas de los ejes X e Y, las barras
y cada columna del histograma mostrar su valor encima, que tenga mejoras en bordes y textos,ajustar tamaños si es necesario.
Usar colores suaves. Realiza otras mejoras si es necesario.
Recordar que estamos trabajando con pandas,Seaborn y Matplotlib  

"""


# SUBMENÚ - GENERAR GRÁFICOS Y REPORTES

def submenu_graficos():
    while True:
        limpiar_consola()
        print("\033[96m" + "═" * 50 + "\033[0m")
        print(" 📊 \033[1mSubmenú - Generar Gráficos\033[0m")
        print("\033[96m" + "═" * 50 + "\033[0m")
        print("1. 📈 Gráfico de líneas (entradas por fecha)")
        print("2. 📊 Gráfico de barras (entradas por título)")
        print("3. 🥧 Gráfico circular (proporción de entradas)")
        print("4. 📉 Histograma (longitud de entradas)")
        print("5. 📋 Mostrar todos los gráficos")
        print("6. ↩️ Volver al menú principal")

        opcion = input("\n👉 Elige una opción: ")

        match opcion:
            case '1':
                grafico_lineas()
            case '2':
                grafico_barras()
            case '3':
                grafico_torta()
            case '4':
                grafico_histograma()
            case '5':
                mostrar_todos_graficos()
            case '6':
                break
            case _:
                print("❌ Opción inválida")
                pausar()
                
#Funcion para cargar datos para generar los graficos:
"""
    Carga los datos del diario desde un archivo JSON y prepara las fechas para análisis y gráficos.
    """
def cargar_datos_diario(nombre_archivo="diario.json"):
    try:
        df = pd.read_json(nombre_archivo, encoding="utf-8") # Lee el archivo JSON usando pandas y lo carga en un DataFrame.
        df["fecha"] = pd.to_datetime(df["fecha"], format="%d-%m-%Y", errors="coerce") # Convierte la columna 'fecha' a objetos datetime para poder trabajar con fechas.`errors="coerce"` convierte valores inválidos a NaT (not a time) en caso de error.
        return df # Devuelve el DataFrame listo para análisis o gráficos.
    except Exception as e:
        print(f"❌ Error al cargar el archivo: {e}")
        return pd.DataFrame() #Devuelve un DataFrame vacío para que el programa pueda continuar sin romperse        

#Funcion para generar Graficos de lineas:
def grafico_lineas():
    df = cargar_datos_diario() # Carga los datos del diario usando la función anterior
    if df.empty:
        print("⚠️ No hay datos para graficar")
        return   # Si el DataFrame está vacío, se avisa al usuario y se sale de la función.

    conteo = df.groupby("fecha").size().reset_index(name="cantidad") 
    # Agrupa los datos por fecha y cuenta cuántas entradas hay por cada fecha.
    # `reset_index(name="cantidad")` convierte el resultado en un DataFrame con columnas 'fecha' y 'cantidad'.

    matp.figure(figsize=(8,4)) # Crea una nueva figura para el gráfico con tamaño 8x4 pulgadas
    sb.lineplot(data=conteo, x="fecha", y="cantidad", marker="o") # Genera un gráfico de líneas con seaborn usando 'fecha' en el eje X y 'cantidad' en el eje Y.
    # `marker="o"` coloca un círculo en cada punto de datos.
    matp.title("Entradas por fecha") # Establece el título del gráfico.
    matp.xticks(rotation=45) # Rota las etiquetas del eje X 45 grados para que se vean mejor.
    matp.tight_layout() # Ajusta automáticamente los márgenes para que nada se superponga
    matp.show()
    
    
#Funcion para generar Graficos de Barras:
def grafico_barras():
# Cargar los datos desde el JSON
    df = cargar_datos_diario()
    if df.empty:
        print("⚠️ No hay datos para graficar")
        return

    # Crear la figura
    matp.figure(figsize=(10, 5))

    # Gráfico de barras ordenado por cantidad de apariciones del título
    ax = sb.countplot(
    data=df,  # Se especifica el DataFrame que contiene los datos
    x="titulo",
    order=df["titulo"].value_counts().index, #Ordena las barras según la cantidad de entradas por título (de mayor a menor)
    color=sb.color_palette("viridis")[0]  # Un solo color de la paleta
)

    # Personalización
    matp.title("Cantidad de entradas por título", fontsize=14) # Establece el título del gráfico con tamaño de fuente 14
    matp.xlabel("Título del diario", fontsize=12) # Etiqueta el eje X con el nombre "Título del diario" y tamaño de fuente 12
    matp.ylabel("Cantidad de entradas", fontsize=12) # Etiqueta el eje Y con el nombre "Cantidad de entradas" y tamaño de fuente 12
    matp.xticks(rotation=45, ha='right') # Rota las etiquetas del eje X 45 grados para que se lean mejor
        # 'ha="right"' alinea las etiquetas hacia la derecha para evitar superposición

    # Agregar los valores arriba de cada barra
    for p in ax.patches: # Recorre cada barra (patch) del gráfico
        height = p.get_height() # Obtiene la altura de la barra, que representa la cantidad de entradas
        ax.text(
            p.get_x() + p.get_width() / 2, # Posición horizontal: centro de la barra
            height + 0.1, # Posición vertical: un poco por encima de la barra
            f"{int(height)}", # Texto a mostrar: la cantidad convertida a entero
            ha='center',  #Centra el texto horizontalmente
            va='bottom',  # Coloca el texto justo arriba de la barra
            fontsize=10,
            color='black'
        )

    # Ajustar espaciado
    matp.tight_layout()

    # Mostrar el gráfico
    matp.show()

        
        
#Funcion para generar Grafico de torta:
def grafico_torta():
    df = cargar_datos_diario()
    if df.empty:
        print("⚠️ No hay datos para graficar")
        return

    conteo = df["titulo"].value_counts() # Cuenta cuántas veces aparece cada título en el diario
    # Devuelve un objeto Series con títulos como índice y cantidad como valores

    matp.figure(figsize=(7,7)) # Crea una figura cuadrada de 7*7 pulgadas para el gráfico de torta
    matp.pie(conteo, labels=conteo.index, autopct="%1.1f%%", startangle=90)  # Muestra porcentaje con 1 decimal en cada porción Rotación inicial del gráfico en grados
    matp.title("Proporción de entradas por título")
    matp.show()
        
#Funcion para generar Grafico Histograma:
def grafico_histograma():
    df = cargar_datos_diario()
    if df.empty:
        print("⚠️ No hay datos para graficar")
        return

    df["longitud"] = df["entrada"].str.len() #Crea una nueva columna 'longitud' que contiene la cantidad de caracteres de cada entrada

    matp.figure(figsize=(8,4)) #Crea una nueva figura de 8*4
    sb.histplot(df["longitud"], bins=10, kde=True, color="skyblue") #bins=10, Número de intervalos (barras) en el histograma, kde=True Añade una curva de densidad estimada sobre el histograma
    matp.title("Distribución de la longitud de las entradas")
    matp.xlabel("Cantidad de caracteres")
    matp.ylabel("Frecuencia")
    matp.tight_layout() # Ajusta automáticamente los márgenes para que no se superpongan elementos
    matp.show() #Muestra el grafico  
    
    
#Funcion que muestra todos los graficos como un grid de 2x2
def mostrar_todos_graficos():
    df = cargar_datos_diario()
    if df.empty:
        print("⚠️ No hay datos para graficar")
        return

    # Aseguramos que 'fecha' sea datetime
    df["fecha"] = pd.to_datetime(df["fecha"], format="%d-%m-%Y", errors="coerce") # Convierte la columna 'fecha' del DataFrame a tipo datetime usando el formato DD-MM-AAAA
# Si algún valor no se puede convertir, se establece como NaT (not a time)
    df = df.dropna(subset=["fecha"]).copy()# Elimina filas donde la columna 'fecha' es NaT
# Se usa copy() para evitar advertencias de pandas sobre modificaciones en vistas
    if df.empty:
        print("⚠️ No hay entradas con fecha válida para graficar.")
        return

    # Columnas auxiliares
    df["longitud"] = df["entrada"].str.len() # Calcula la longitud de cada entrada (cantidad de caracteres) y la guarda en una nueva columna
    df["mes"] = df["fecha"].dt.month # Extrae el mes de la fecha y lo almacena en una nueva columna
    df["dia"] = df["fecha"].dt.day  # Extrae el día de la fecha y lo almacena en otra columna

    fig, axes = matp.subplots(2, 2, figsize=(14, 10)) # Crea una figura con 2 filas y 2 columnas de subgráficos
    fig.suptitle(" Resumen general del Diario", fontsize=16, fontweight="bold")  #Coloca un título general para toda la figura

    # -- 1 Entradas por fecha (línea)
    conteo_fecha = df.groupby("fecha").size().sort_index() # Agrupa los datos por fecha y cuenta cuántas entradas hay por fecha y las ordena.
    axes[0, 0].plot(conteo_fecha.index, conteo_fecha.values, marker="o", color="royalblue")
    axes[0, 0].set_title("Evolución de entradas por fecha")
    axes[0, 0].set_xlabel("Fecha")
    axes[0, 0].set_ylabel("Cantidad de entradas")
    axes[0, 0].tick_params(axis='x', rotation=45) # Rota las etiquetas del eje X 45 grados para mejor legibilidad
    axes[0, 0].grid(True, linestyle="--", alpha=0.5) # Añade una cuadrícula con líneas punteadas y transparencia media

    # ---  Distribución de longitudes (histograma)
    n, bins, patches = axes[0, 1].hist(df["longitud"], bins=10, color="orange", edgecolor="black")# Crea un histograma de las longitudes de las entradas
# n = frecuencia, bins = límites de los intervalos, patches = objetos de las barras
    axes[0, 1].set_title("Distribución de longitudes de las entradas")
    axes[0, 1].set_xlabel("Longitud del texto (caracteres)")
    axes[0, 1].set_ylabel("Frecuencia")

    #  Mostrar números encima de cada barra del histograma
    for i in range(len(n)):
        axes[0, 1].text(
            (bins[i] + bins[i+1]) / 2,  # posición X centrada
            n[i] + 0.2,                 # posición Y un poco arriba
            int(n[i]),                  # el número
            ha='center', va='bottom', fontsize=9
        )

    axes[0, 1].grid(True, linestyle="--", alpha=0.5) # Añade cuadrícula al histograma

    # ---  Entradas por mes (barras)
    meses_counts = df["mes"].value_counts().sort_index()  #Cuenta cuántas entradas hay por mes y ordena por mes
    if not meses_counts.empty:
        meses_idx = meses_counts.index.tolist()
        meses_labels = [calendar.month_abbr[m] for m in meses_idx]  # Convierte los números de mes a nombres abreviados (Ene, Feb, etc.)
        bars = axes[1, 0].bar(meses_labels, meses_counts.values, color="seagreen", edgecolor="black")  #Crea un gráfico de barras de entradas por mes
        axes[1, 0].set_title("Entradas por mes")
        axes[1, 0].set_xlabel("Mes")
        axes[1, 0].set_ylabel("Cantidad de entradas")
        axes[1, 0].grid(axis="y", linestyle="--", alpha=0.5) # Configura títulos, etiquetas y cuadrícula del gráfico de barras

        #  Mostrar número encima de cada barra
        for bar in bars:
            height = bar.get_height()
            axes[1, 0].text(
                bar.get_x() + bar.get_width()/2,
                height + 0.1,
                f"{int(height)}",
                ha='center', va='bottom', fontsize=9
            )
    else:
        axes[1, 0].text(0.5, 0.5, "No hay datos por mes", ha="center")

    # ---  Gráfico de torta de entradas por título
    titulo_counts = df["titulo"].value_counts() # Cuenta cuántas veces aparece cada título
    if not titulo_counts.empty:
        if len(titulo_counts) > 8:  # Si hay más de 8 títulos, agrupa los restantes en "Otros"
            top = titulo_counts.head(8)
            others = titulo_counts.iloc[8:].sum()
            top["Otros"] = others
            pie_counts = top
        else:
            pie_counts = titulo_counts # Si hay 8 o menos títulos, se usan todos

        axes[1, 1].pie(
            pie_counts.values,  # Valores de cada porción
            labels=pie_counts.index,   # Etiquetas de cada porción
            autopct="%1.1f%%", # Porcentaje mostrado en cada porción
            startangle=140, # Rotación inicial del gráfico
            colors=sb.color_palette("pastel") #colores de cada porcion
        )
        axes[1, 1].set_title("Proporción de entradas por título") # Título y ajuste para que la torta sea circular
        axes[1, 1].axis("equal")
    else:
        axes[1, 1].text(0.5, 0.5, "No hay títulos para mostrar", ha="center") # Mensaje si no hay títulos para mostrar en el gráfico de torta

    matp.tight_layout(rect=[0, 0, 1, 0.96]) # Ajusta los márgenes y espacio entre subgráficos, dejando espacio arriba para el título general

    matp.show()


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
                cargar_diario_json()
            case '8':
                GenerarDatos_aleatorio()
            case '9':
                submenu_graficos()      
            case '10':  # Salir
                salir()
                break
            case _:  # Caso por defecto si no coincide ninguna opción
                print("Opción inválida, intenta nuevamente.")
                input("Presiona Enter para continuar...")



# Bloque principal que ejecuta el menú si este archivo se corre directamente
if __name__ == "__main__":
    main()    