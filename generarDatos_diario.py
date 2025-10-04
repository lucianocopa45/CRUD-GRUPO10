# Importamos librerías necesarias
import os      # Para limpiar la consola según el sistema operativo
import json     # Para leer y escribir archivos json
import time
import pandas as pd #Para analizar y mostrar los datos en formato de tablas
import random #Para seleccionar datoss aleatorios
from datetime import datetime, timedelta #Para generar Fechas aleatorias en los ultimos 365 dias
import matplotlib.pyplot as matp #Matplolib: crea los graficos
import seaborn as sb #seaborn: Crea graficos estadisticos mas esteticos que Matplotlib
import calendar



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
    else:
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
    
#Funcion para actualizar el contenido de un Diario:
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
        nombre_archivo = "diario.json"
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(diario, archivo, ensure_ascii=False, indent=4)  # 👈 Guardar con formato bonito
        print(f"\n✅ Diario guardado correctamente en '{nombre_archivo}' ✅")
    except Exception as e:
        print(f"❌ Error al guardar el diario: {e} ❌")

    pausar()



# ──────────────────────────────────────────────
# Función para cargar el diario desde archivo JSON
# ──────────────────────────────────────────────
def cargar_diario_json():
    limpiar_consola()
    print("\033[96m" + "═" * 50 + "\033[0m")
    print(" 📂 \033[1mCargar Diario desde archivo JSON\033[0m 📂")
    print("\033[96m" + "═" * 50 + "\033[0m")

    try:
        nombre_archivo = "diario.json"
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)   # Leer JSON
            diario.clear()
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
        df_existente = pd.read_json("diario.json")
        diario = df_existente.to_dict(orient="records")  # Convertimos a lista de diccionarios
    except FileNotFoundError:
        diario = []  # Si no existe el archivo, empezamos con lista vacía
    
    try:
        cantidad = int(input("Ingrese la cantidad de datos a generar: "))
    except ValueError:
        print("❌ Entrada inválida. Debe ingresar un número entero.")
        return  # sale de la función si hay error

    # Generar datos aleatorios
    fechas = generar_fechas_aleatorias(cantidad)
    titulos = [random.choice(titulos_ejemplos) for _ in range(cantidad)]
    entradas = [random.choice(entradas_ejemplos) for _ in range(cantidad)]

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
def cargar_datos_diario(nombre_archivo="diario.json"):
    try:
        df = pd.read_json(nombre_archivo, encoding="utf-8")
        df["fecha"] = pd.to_datetime(df["fecha"], format="%d-%m-%Y", errors="coerce")
        return df
    except Exception as e:
        print(f"❌ Error al cargar el archivo: {e}")
        return pd.DataFrame()              

#Funcion para generar Graficos de lineas:
def grafico_lineas():
    df = cargar_datos_diario()
    if df.empty:
        print("⚠️ No hay datos para graficar")
        return

    conteo = df.groupby("fecha").size().reset_index(name="cantidad")

    matp.figure(figsize=(8,4))
    sb.lineplot(data=conteo, x="fecha", y="cantidad", marker="o")
    matp.title("Entradas por fecha")
    matp.xticks(rotation=45)
    matp.tight_layout()
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
    data=df,
    x="titulo",
    order=df["titulo"].value_counts().index,
    color=sb.color_palette("viridis")[0]  # Un solo color de la paleta
)

    # Personalización
    matp.title("Cantidad de entradas por título", fontsize=14)
    matp.xlabel("Título del diario", fontsize=12)
    matp.ylabel("Cantidad de entradas", fontsize=12)
    matp.xticks(rotation=45, ha='right')

    # Agregar los valores arriba de cada barra
    for p in ax.patches:
        height = p.get_height()
        ax.text(
            p.get_x() + p.get_width() / 2,
            height + 0.1,
            f"{int(height)}",
            ha='center',
            va='bottom',
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

    conteo = df["titulo"].value_counts()

    matp.figure(figsize=(6,6))
    matp.pie(conteo, labels=conteo.index, autopct="%1.1f%%", startangle=90)
    matp.title("Proporción de entradas por título")
    matp.show()
        
#Funcion para generar Grafico Histograma:
def grafico_histograma():
    df = cargar_datos_diario()
    if df.empty:
        print("⚠️ No hay datos para graficar")
        return

    df["longitud"] = df["entrada"].str.len()

    matp.figure(figsize=(8,4))
    sb.histplot(df["longitud"], bins=10, kde=True, color="skyblue")
    matp.title("Distribución de la longitud de las entradas")
    matp.xlabel("Cantidad de caracteres")
    matp.ylabel("Frecuencia")
    matp.tight_layout()
    matp.show()   
    
    
#Funcion que muestra todos los graficos como un grid de 2x2
def mostrar_todos_graficos():
    import calendar
import pandas as pd
import matplotlib.pyplot as matp
import seaborn as sb

def mostrar_todos_graficos():
    df = cargar_datos_diario()
    if df.empty:
        print("⚠️ No hay datos para graficar")
        return

    # Aseguramos que 'fecha' sea datetime
    df["fecha"] = pd.to_datetime(df["fecha"], format="%d-%m-%Y", errors="coerce")
    df = df.dropna(subset=["fecha"]).copy()
    if df.empty:
        print("⚠️ No hay entradas con fecha válida para graficar.")
        return

    # Columnas auxiliares
    df["longitud"] = df["entrada"].str.len()
    df["mes"] = df["fecha"].dt.month
    df["dia"] = df["fecha"].dt.day

    fig, axes = matp.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("📊 Resumen general del Diario", fontsize=16, fontweight="bold")

    # -- 1 Entradas por fecha (línea)
    conteo_fecha = df.groupby("fecha").size().sort_index()
    axes[0, 0].plot(conteo_fecha.index, conteo_fecha.values, marker="o", color="royalblue")
    axes[0, 0].set_title("Evolución de entradas por fecha")
    axes[0, 0].set_xlabel("Fecha")
    axes[0, 0].set_ylabel("Cantidad de entradas")
    axes[0, 0].tick_params(axis='x', rotation=45)
    axes[0, 0].grid(True, linestyle="--", alpha=0.5)

    # ---  Distribución de longitudes (histograma)
    n, bins, patches = axes[0, 1].hist(df["longitud"], bins=10, color="orange", edgecolor="black")
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

    axes[0, 1].grid(True, linestyle="--", alpha=0.5)

    # ---  Entradas por mes (barras)
    meses_counts = df["mes"].value_counts().sort_index()
    if not meses_counts.empty:
        meses_idx = meses_counts.index.tolist()
        meses_labels = [calendar.month_abbr[m] for m in meses_idx]
        bars = axes[1, 0].bar(meses_labels, meses_counts.values, color="seagreen", edgecolor="black")
        axes[1, 0].set_title("Entradas por mes")
        axes[1, 0].set_xlabel("Mes")
        axes[1, 0].set_ylabel("Cantidad de entradas")
        axes[1, 0].grid(axis="y", linestyle="--", alpha=0.5)

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
    titulo_counts = df["titulo"].value_counts()
    if not titulo_counts.empty:
        if len(titulo_counts) > 8:
            top = titulo_counts.head(8)
            others = titulo_counts.iloc[8:].sum()
            top["Otros"] = others
            pie_counts = top
        else:
            pie_counts = titulo_counts

        axes[1, 1].pie(
            pie_counts.values,
            labels=pie_counts.index,
            autopct="%1.1f%%",
            startangle=140,
            colors=sb.color_palette("pastel")
        )
        axes[1, 1].set_title("Proporción de entradas por título")
        axes[1, 1].axis("equal")
    else:
        axes[1, 1].text(0.5, 0.5, "No hay títulos para mostrar", ha="center")

    matp.tight_layout(rect=[0, 0, 1, 0.96])
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