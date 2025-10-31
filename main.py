import os

# Funcion para manejar el menu principal mediante un match/case
def mostrar_menu():
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
        
def crear_pais(nombre,poblacion,superficie,continente):

    return {
        "nombre": nombre.strip().title(),
        "poblacion": int(poblacion),
        "superficie": int(superficie),
        "continente": continente.strip().title()
    }

print(carga_inicial())

            
        
        
