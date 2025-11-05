import os

def actualizar_pais(paises): # AGREGAR VALIDACIONES
    print("Poblacion / Superficie")
    print("P - Poblacion")
    print("S - Superficie")
    
    opcion = input("Seleccione una opción: ").strip().upper()
    
    if opcion not in ["P", "S"]:
        print("Opción inválida.")
        return
        
    
    resultado = buscar_pais(paises)

    pais = resultado[0]

    if opcion == "P":
        nueva_poblacion = pedir_num("Ingrese la nueva población: ")
        pais["poblacion"] = nueva_poblacion
        print(f"La población de {pais['nombre']} ha sido actualizada a {nueva_poblacion}.")

    elif opcion == "S":
        nueva_superficie = pedir_num("Ingrese la nueva superficie: ")
        pais["superficie"] = nueva_superficie
        print(f"La superficie de {pais['nombre']} ha sido actualizada a {nueva_superficie}.")
    

def filtrar_paises(paises): # AGREGAR VALIDACIONES
    filtro = input("Ingrese por que criterio desea filtrar (C/P/S): ").strip().upper()
    if filtro not in ["C", "P", "S"]:
        print("Opción inválida.")
        return
    
    match filtro:
    
        case "C":
            continente = normalizar_string(pedir_string("Ingrese el continente por el cual desea filtrar: "))
            resultados = []
            for pais in paises:
                if pais["continente"] == continente:
                    resultados.append(pais)
                    
            if not resultados:
                print("No se encontraron países en ese continente.")
                return
            else:
                print (f"Estos son los países del continente {continente}:")
                print (resultados)

        case "P":
            poblacion_min = pedir_num("Ingrese la población mínima: ")
            poblacion_max = pedir_num("Ingrese la población máxima: ")
            resultados = []
            if poblacion_min > poblacion_max:
                print("El valor mínimo no puede ser mayor al máximo.")
                return
            for pais in paises:
                if poblacion_min <= pais["poblacion"] and pais["poblacion"]<= poblacion_max:
                    resultados.append(pais)
            if not resultados:
                print("No se encontraron países en ese rango de población.")
                return
            else:
                print (f"Estos son los paises con la poblacion entre {poblacion_min} y {poblacion_max}:")
                print (resultados)
                

        case "S":
            superficie_min = pedir_num("Ingrese la superficie mínima: ")
            superficie_max = pedir_num("Ingrese la superficie máxima: ")
            resultados = []
            if superficie_min > superficie_max:
                print("El valor mínimo no puede ser mayor al máximo.")
                return
            for pais in paises:
                if superficie_min <= pais["superficie"] and pais["superficie"]<= superficie_max:
                    resultados.append(pais)
            if not resultados:
                print("No se encontraron países en ese rango de superficie.")
                return
            else:
                print (f"Estos son los paises con la superficie entre {superficie_min} y {superficie_max}:")
                print (resultados)
    

# Funcion para manejar el menu principal mediante un match/case
def mostrar_menu(paises):
    while True:
        opcion = int(input("""
    Bienvenido al programa de gestión de paises!
    Elija su opción:
    1. Agregar país
    2. Actualizar datos de un país
    3. Buscar un país
    4. Filtrar países
    5. Ordenar países
    6. Mostrar estadísticas
    7. Salir
    """))
        
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
        
# Funcion para realizar la carga inicial de datos en la lista 
def carga_inicial():

    paises = []

    if not os.path.exists("paises.csv"):
        # Si no existe, lo creamos vacío con el encabezado
        with open("paises.csv", "w") as archivo:
            archivo.write("nombre,poblacion,superficie,continente\n")
        print("No se encontró el archivo 'paises.csv'. Se creó uno nuevo.")
        return []

    with open("paises.csv", "r") as archivo:

        next(archivo) # Saltamos la primera linea (encabezado)
        for linea in archivo:
            if linea.strip() == "":
                continue

            nombre, poblacion, superficie, continente = linea.strip().split(",")

            pais = crear_pais(nombre,poblacion,superficie,continente)

            paises.append(pais) # Agregamos el diccionario a la lista principal
    
    return paises

# Funcion pedir texto y validar que no esté vacío.
def pedir_string(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto.strip() == "":
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

# Funcion para actualizar csv
def actualizar_csv(paises):
    """
    Reescribe el archivo 'paises.csv' con la lista actual en memoria.

    Cada vez que se llama esta función, se itera sobre la lista de países
    y se sobrescribe completamente el archivo, garantizando consistencia
    con el estado actual en memoria.
    """

    with open("paises.csv", "w") as archivo:

        archivo.write("nombre,poblacion,superficie,continente\n")

        for pais in paises:
            nombre = pais["nombre"]
            poblacion = pais["poblacion"]
            superficie = pais["superficie"]
            continente = pais["continente"]

            archivo.write(f"{nombre},{poblacion},{superficie},{continente}\n")

# Funcion para crear un pais, se pasan por parametro todos los datos y se devuelve un diccionario con todos los datos del pais        
def crear_pais(nombre,poblacion,superficie,continente):
    """
    Crea un diccionario que representa un país con sus datos estandarizados.

    Limpia espacios, aplica formato de título en el nombre y continente,
    y convierte los valores numéricos a su tipo correspondiente.
    """

    return {
        "nombre": normalizar_string(nombre.title()),
        "poblacion": int(poblacion),
        "superficie": int(superficie),
        "continente": normalizar_string(continente.title())
    }

# Funcion para agregar un pais al csv.
def agregar_pais(paises): 
    """
    Solicita los datos de un nuevo país por consola y lo agrega a la lista en memoria.

    Interactúa con el usuario para obtener los datos del país, crea un diccionario
    formateado mediante la función `crear_pais()` y lo añade a la lista existente.
    """

    nombre = normalizar_string(pedir_string("Ingrese el nombre del país: "))
    poblacion = pedir_num("Ingrese la población del país: ")     
    superficie = pedir_num("Ingrese la superficie del país: ")
    continente = normalizar_string(pedir_string("Ingrese el continente al que pertenece el país: "))

    pais = crear_pais(nombre,poblacion,superficie,continente)
    paises.append(pais)

    actualizar_csv(paises)

# Funcion para buscar un país
def buscar_pais(paises):
    entrada_usuario = normalizar_string(pedir_string("Ingrese el nombre del país que desea buscar: "))

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

def buscar_pais_imp(paises):
    resultados = buscar_pais(paises)
    # Mostramos los resultados en caso de que haya
    if not resultados:
        print("No se encontraron países con ese nombre.")
    else:
        print(f"\nSe encontraron {len(resultados)} resultado(s):")
        for pais in resultados:
            print(f"- {pais['nombre']} (Población: {pais['poblacion']}, Superficie: {pais['superficie']}, Continente: {pais['continente']})")

# Funcion para ordenar paises
def ordenar_paises(paises, campo, descendente=False):

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

def ordenar_paises_impl(paises): # AGREGAR VALIDACIONES
    opcion = pedir_num("""
    Ordenar por:
    1. Nombre
    2. Población
    3. Superficie
                       
    """)
    
    resultados = []

    match opcion:
        case 1:
            resultados = ordenar_paises(paises, 'nombre')
        case 2:
            resultados = ordenar_paises(paises, 'poblacion')
        case 3:
            # Si selecciona la opcion de superficie, preguntamos si quiere en forma ascendente o descendente
            opcion = pedir_num("""
            Ordenar de forma:
            1. Ascendente
            2. Descendente

            """)
            if opcion == 1:
                resultados = ordenar_paises(paises, 'superficie')
            elif opcion == 2:
                resultados = ordenar_paises(paises, 'superficie', True)
        case _:
            print("Opción inválida.")
            return
    
    print("\n==== LISTA ORDENADA ====")
    for pais in resultados:
        print(f"- {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} | Continente: {pais['continente']}")

# ==== Funciones para calcular estadisticas ====

def pais_mayor_poblacion(paises):
    mayor_pais = paises[0]
    for pais in paises:
        if pais['poblacion'] > mayor_pais['poblacion']:
            mayor_pais = pais

    return mayor_pais

def pais_menor_poblacion(paises):
    menor_pais = paises[0]
    for pais in paises:
        if pais['poblacion'] < menor_pais['poblacion']:
            menor_pais = pais

    return menor_pais

def promedio(paises, campo):
    total = 0
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
                       
# ==================== MAIN ======================

paises = carga_inicial() 
print(paises)           # TEST
mostrar_menu(paises)       
print(carga_inicial())  # TEST


            
        
        
