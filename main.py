import os

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

# ==================== MAIN ======================

paises = carga_inicial() 
print(paises)           # TEST
mostrar_menu(paises)       
print(carga_inicial())  # TEST


            
        
        
