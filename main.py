import csv
import os
import csv

# ===================================================
# FUNCIONES DE UTILIDAD (Validación y Normalización)
# ===================================================

# Funcion pedir texto, normalizarlo y validar que no esté vacío.
def pedir_string(mensaje):
    while True:
        texto = normalizar_string(input(mensaje))
        if not texto or texto.isdigit():
            print("Por favor, ingrese un texto válido.")
        else:
            return texto
        
#  Funcion para pedir un numero y verificar que sea válido.
def pedir_num(mensaje):
    while True:
        entrada = input(mensaje).strip()

        if not entrada.isdigit():
            print("Por favor, ingrese un número entero válido.")
            continue

        numero = int(entrada)

        if numero == 0:
            print("Por favor, ingrese un número distinto de 0")
        else:
            return numero
        
# Funcion para normalizar todos los textos que se ingresan, asegurando constancia
def normalizar_string(texto):
    return " ".join(texto.lower().split()).title()

# Funcion para validar que la lista no este vacia
def validar_lista_no_vacia(paises, mensaje_error="No hay países en la base de datos"):
    if not paises:
        print(mensaje_error)
        return False
    return True

# =======================================================
#         FUNCIONES DE GESTIÓN DE ARCHIVOS (CSV)
# =======================================================

# Funcion para realizar la carga inicial de datos en la lista 
def carga_inicial():

    paises = []
    archivo_nombre = "paises.csv"

    if not os.path.exists(archivo_nombre):
        return []

    with open(archivo_nombre, "r", newline="", encoding="utf-8") as archivo:

        reader = csv.reader(archivo)

        encabezado = next(reader, None)  # Saltamos el encabezado

        # Si no hay encabezado, el archivo está vacío
        if encabezado is None:
            print(f"Advertencia: El archivo '{archivo_nombre}' está vacío. Se iniciará con lista vacía.")
            return []
        
        # Validar que el encabezado tenga las columnas correctas 
        if len(encabezado) != 4:
            print(f"Advertencia: El encabezado del archivo no tiene el formato esperado.")
            print(f"Se esperaban 4 columnas (nombre, poblacion, superficie, continente).")
            return []

        # Usamos enumerate para saber el número de línea en caso de error
        for i, linea in enumerate(reader):
            if not linea:
                continue 

            # Asumimos 4 columnas, si no, es un error de formato
            if len(linea) != 4:
                print(f"Error: Línea {i+2} malformada. Se omitió.")
                continue

            nombre, poblacion_str, superficie_str, continente = linea

            if not poblacion_str.isdigit() or not superficie_str.isdigit():
                print(f"Error: Datos numéricos inválidos en línea {i+2} ('{nombre}'). Se omitió.")
                continue
            
            # Si pasa la validación, convertimos
            poblacion_int = int(poblacion_str)
            superficie_int = int(superficie_str)
            pais = crear_pais(nombre, poblacion_int, superficie_int, continente)
            paises.append(pais)
    
    return paises

# Funcion para actualizar csv
def actualizar_csv(paises):
    """
    Reescribe el archivo 'paises.csv' con la lista actual en memoria
    usando csv.DictWriter.
    """
    archivo_nombre = "paises.csv"
    
    campos = ["nombre", "poblacion", "superficie", "continente"]

    with open(archivo_nombre, "w", newline="", encoding="utf-8") as archivo:

        # Usamos DictWriter para escribir diccionarios directamente
        writer = csv.DictWriter(archivo, fieldnames=campos)

        # Escribimos el encabezado
        writer.writeheader()

        # Escribimos las filas desde la lista de diccionarios
        writer.writerows(paises)

# =======================================================
#         FUNCIONES PRINCIPALES (CRUD)
# =======================================================
    
def crear_pais(nombre,poblacion,superficie,continente):
    """
    Crea un diccionario que representa un país con sus datos estandarizados.

    Limpia espacios, aplica formato de título en el nombre y continente,
    y convierte los valores numéricos a su tipo correspondiente.
    """

    return {
        "nombre": normalizar_string(nombre.title()),
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": normalizar_string(continente.title())
    }

# Funcion para agregar un pais al csv.
def agregar_pais(paises): 
    """
    Solicita los datos de un nuevo país por consola y lo agrega a la lista en memoria en caso de que no exista.

    Interactúa con el usuario para obtener los datos del país, crea un diccionario
    formateado mediante la función `crear_pais()` y lo añade a la lista existente.
    Finalmente, actualiza el archivo CSV para reflejar el nuevo estado de la lista.
    """


    nombre = pedir_string("Ingrese el nombre del país: ")
    for p in paises:
        if normalizar_string(nombre) == normalizar_string(p["nombre"]):
            print("El país ya existe en la base de datos.")
            return
    
    poblacion = pedir_num("Ingrese la población del país: ")     
    superficie = pedir_num("Ingrese la superficie del país: ")
    continente = pedir_string("Ingrese el continente al que pertenece el país: ")

    pais = crear_pais(nombre,poblacion,superficie,continente)

    paises.append(pais)

    actualizar_csv(paises)
    print(f"El país {pais['nombre']} ha sido agregado exitosamente.")

# Funcion para buscar un país
def buscar_pais(paises):
    entrada_usuario = pedir_string("Ingrese el nombre del país que desea buscar: ")

    resultados = [] # Creamos lista para agregar todas las coincidencias

    # Iteramos sobre la lista de paises original y agregamos todas las coincidencias a resultados
    for pais in paises:
        if entrada_usuario in pais["nombre"]:
            resultados.append(pais)

    # Mostramos los resultados en caso de que haya
    if not resultados:
        return None
    else:
        return resultados

# Funcion para buscar un país e imprimir resultados
def buscar_pais_imp(paises):
    resultados = buscar_pais(paises)
    # Mostramos los resultados en caso de que haya
    if not resultados:
        print("No se encontraron países con ese nombre.")
    else:
        print(f"\nSe encontraron {len(resultados)} resultado(s):")
        for pais in resultados:
            print(f"- {pais['nombre']} (Población: {pais['poblacion']}, Superficie: {pais['superficie']}, Continente: {pais['continente']})")

# Funcion para actualizar pais
def actualizar_pais(paises): 
    print("Que deseas actualizar?")
    print("Poblacion / Superficie")
    print("P - Poblacion")
    print("S - Superficie")

    # Validamos la opcion ingresada
    while True:
        opcion = pedir_string("Seleccione una opción: ")
        if opcion not in ["P", "S"]:
            print("Opción inválida.")
        else:
            break

    # Buscamos el pais a actualizar
    resultado = buscar_pais(paises)
    if not resultado:
        print("No se encontró el país indicado.")
        return

    paises_encontrados = resultado
    
    print(f"\nSe encontraron {len(paises_encontrados)} pais(es):")
    for i in enumerate(paises_encontrados):

        print(f"{i[0]+1}. {paises_encontrados[i[0]]['nombre']} (Población: {paises_encontrados[i[0]]['poblacion']}, Superficie: {paises_encontrados[i[0]]['superficie']}, Continente: {paises_encontrados[i[0]]['continente']})")
    
    if len(paises_encontrados) > 1:
        
        while True:
            posicion_actualizar = pedir_num("Ingrese el numero del pais que desea actualizar: ") - 1
            
            if posicion_actualizar < 0 or posicion_actualizar >= len(paises_encontrados):
                print("Posición inválida.")
            
            else:
                break
    else:
        posicion_actualizar = 0

    pais = paises_encontrados[posicion_actualizar]


    if opcion == "P":
        nueva_poblacion = pedir_num("Ingrese la nueva población: ")
        pais["poblacion"] = nueva_poblacion
        print(f"La población de {pais['nombre']} ha sido actualizada a {nueva_poblacion}.")

    elif opcion == "S":
        nueva_superficie = pedir_num("Ingrese la nueva superficie: ")
        pais["superficie"] = nueva_superficie
        print(f"La superficie de {pais['nombre']} ha sido actualizada a {nueva_superficie}.")

    actualizar_csv(paises)

# =======================================================
#                 FUNCIONES DE FILTRADO
# =======================================================

# Funcion para filtrar paises por continente
def filtrar_continente(paises):
    continente = pedir_string("Ingrese el continente por el cual desea filtrar: ")
    resultados = []
    # Filtramos los paises que se encuentren en el continente indicado
    for pais in paises:
        if pais["continente"] == continente:
            resultados.append(pais)
    
    if not resultados:
        print("No se encontraron países en ese continente.")
        return
    # Mostramos paises encontrados en el continente
    else:
        print (f"Estos son los países del continente {continente}:")
        for pais in resultados:
            print(f"- {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} | Continente: {pais['continente']}")

def validar_rango(tipo_dato):
    """Valida que el mínimo no sea mayor al máximo"""
    while True:
        minimo = pedir_num(f"Ingrese {tipo_dato} mínima: ")
        maximo = pedir_num(f"Ingrese {tipo_dato} máxima: ")
        if minimo > maximo:
            print("El valor mínimo no puede ser mayor al máximo.")
        else:
            return minimo, maximo

# Filtrar por poblacion
def filtrar_poblacion(paises):
    resultados = []

    # Verificamos que la poblacion minima no sea mayor a la maxima
    poblacion_min, poblacion_max = validar_rango("población")
    
    # Recorremos paises y guardamos en la lista los que cumplan la condicion
    for pais in paises:
            if poblacion_min <= pais["poblacion"] and pais["poblacion"]<= poblacion_max:
                    resultados.append(pais)

    # Si existen, los devolvemos
    if not resultados:
        print("No se encontraron países en ese rango de población.")
        return
    else:
        print (f"Estos son los paises con la poblacion entre {poblacion_min} y {poblacion_max}:")
        for pais in resultados:
            print(f"- {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} | Continente: {pais['continente']}")

# Filtrar paises por superficie
def filtrar_superficie(paises):

    resultados = []

    # Validamos que la superficie minima no sea mayor a la maxima
    superficie_min, superficie_max = validar_rango("superficie")

    for pais in paises:
        if superficie_min <= pais["superficie"] and pais["superficie"]<= superficie_max:
            resultados.append(pais)

    if not resultados:
        print("No se encontraron países en ese rango de superficie.")
        return
    else:
        print (f"Estos son los paises con la superficie entre {superficie_min} y {superficie_max}:")
        for pais in resultados:
            print(f"- {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} | Continente: {pais['continente']}")


def filtrar_paises(paises): 
    while True:
        filtro = input("Ingrese por que criterio desea filtrar (C - Continente / P - Población / S - Superficie): ").strip().upper()
        if filtro not in ["C", "P", "S"]:
            print("Opción inválida.")
        else:
            break
    
    match filtro:
    
        case "C":
            filtrar_continente(paises)
        case "P":
            filtrar_poblacion(paises)
        case "S":
            filtrar_superficie(paises)
        
# =======================================================
#         FUNCIONES DE ORDENAMIENTO
# =======================================================

# Funcion para ordenar paises
def ordenar_paises(paises, campo, descendente=False):
    if not validar_lista_no_vacia(paises):
        return []

    # Sacamos cantidad de elementos de la lista
    cant_elementos = len(paises)
    # Copiamos elementos a otra lista para no modificar la lista original
    lista_ordenada = paises.copy()

    # Primer bucle
    for i in range(cant_elementos - 1):
        hubo_cambio = False
        # Segundo bucle
        for j in range(cant_elementos - 1 - i):
            # Pasamos los campos actuales para mayor legibilidad
            a = lista_ordenada[j][campo]
            b = lista_ordenada[j + 1][campo]

            # Si a es String, lo pasamos a minusculas
            if isinstance(a, str):
                a, b = a.lower(), b.lower()

            # Evaluamos dos opciones, si descendente es falso, significa que debemos ordenar de forma ascendente (verificando si a > b)
            # Si descendente es verdadero, significa que debemos ordenar de forma descendente (verificando a < b)
            if (a > b and not descendente) or (a < b and descendente):
                lista_ordenada[j], lista_ordenada[j+1] = lista_ordenada[j + 1], lista_ordenada[j]
                hubo_cambio = True
        # Si no hubo ningun cambio rompemos el bucle para no seguir recorriendo innecesariamente
        if not hubo_cambio:
            break
    return lista_ordenada

def ordenar_paises_impl(paises):
    resultados = []   
    while True:
        opcion = pedir_num("""
        Ordenar por:
        1. Nombre
        2. Población
        3. Superficie
                        
        """)
    
        match opcion:
            case 1:
                resultados = ordenar_paises(paises, 'nombre')
                break
            case 2:
                resultados = ordenar_paises(paises, 'poblacion')
                break
            case 3:
                # Si selecciona la opcion de superficie, preguntamos si quiere en forma ascendente o descendente
                while True:
                    opcion = pedir_num("""
                    Ordenar de forma:
                    1. Ascendente
                    2. Descendente

                    """)
                    if opcion == 1:
                        resultados = ordenar_paises(paises, 'superficie')
                        break
                    elif opcion == 2:
                        resultados = ordenar_paises(paises, 'superficie', True)
                        break
                    else:
                        print("Opción inválida.")
                        continue
            case _:
                print("Opción inválida.")
                continue
        break                
    
    print("\n==== LISTA ORDENADA ====")
    for pais in resultados:
        print(f"- {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} | Continente: {pais['continente']}")

# =======================================================
#               FUNCIONES DE ESTADISTICAS
# =======================================================

def pais_mayor_poblacion(paises):
    if not validar_lista_no_vacia(paises):
        return None

    mayor_pais = paises[0]
    for pais in paises:
        if pais['poblacion'] > mayor_pais['poblacion']:
            mayor_pais = pais

    return mayor_pais

def pais_menor_poblacion(paises):
    if not validar_lista_no_vacia(paises):
        return None

    menor_pais = paises[0]
    for pais in paises:
        if pais['poblacion'] < menor_pais['poblacion']:
            menor_pais = pais

    return menor_pais

# Funcion para calcular el promedio, en este caso necesitamos saber de población y superficie
def promedio(paises, campo):
    total = 0

    if not validar_lista_no_vacia(paises, f"No hay países para calcular el promedio de {campo}"):
        return 0

    for pais in paises:
        total += pais[campo]
    
    promedio = total / len(paises)
    return promedio

def paises_por_continente(paises):
    # Creamos contador para almacenar los continentes con sus cantidades de paises
    contador = {}

    for pais in paises:
        continente = normalizar_string(pais['continente'])
        # Con get obtenemos el valor actual de paises para ese continente, si no existe todavia, lo inicializamos en 0, finalmente le sumamos 1
        contador[continente] = contador.get(continente, 0) + 1

    return contador

def mostrar_estadisticas(paises):
    if not validar_lista_no_vacia(paises, "No hay datos suficientes para mostrar estadísticas."):
        return

    pais_mayor = pais_mayor_poblacion(paises)
    pais_menor = pais_menor_poblacion(paises)
    continentes = paises_por_continente(paises)  

    print("===================== ESTADÍSTICAS ACTUALES =====================")
    print(f"País con mayor población: {pais_mayor['nombre']} | {pais_mayor['poblacion']} habitantes")
    print(f"País con menor población: {pais_menor['nombre']} | {pais_menor['poblacion']} habitantes")
    print(f"Promedio de población: {promedio(paises, 'poblacion')}")
    print(f"Promedio de superficie: {promedio(paises, 'superficie')}")
    print("\nCantidad de países por continente:")

    for continente, cantidad in continentes.items():
        print(f" - {continente}: {cantidad}")

    print("=================================================================\n")

# =======================================================
#               FUNCIÓN PRINCIPAL (MENÚ)
# =======================================================

def mostrar_menu(paises):
    while True:
        opcion = pedir_num("""
    Bienvenido al programa de gestión de paises!
    Elija su opción:
    1. Agregar país
    2. Actualizar datos de un país
    3. Buscar un país
    4. Filtrar países
    5. Ordenar países
    6. Mostrar estadísticas
    7. Salir
    """)
        
        match opcion:
            case 1: 
                agregar_pais(paises)
            case 2:
                actualizar_pais(paises)
            case 3: 
                buscar_pais_imp(paises)
            case 4:
                filtrar_paises(paises)
            case 5:
                ordenar_paises_impl(paises)
            case 6:
                mostrar_estadisticas(paises)
            case 7:
                break
            case _:
                print("Opción inválida. Por favor, intente de nuevo.")

# =======================================================
#                          MAIN
# =======================================================

paises = carga_inicial() 
mostrar_menu(paises)