# (TPI Programación 1)

El objetivo principal de este trabajo practico integrar es aplicar los conocimientos fundamentales de Python para desarrollar un sistema de consola capaz de gestionar un conjunto de datos de países, implementando funcionalidades de filtrado, ordenamiento y cálculo de estadísticas.

## Datos de la Universidad y la Cátedra

**Universidad:** Universidad Tecnológica Nacional (UTN)
**Cátedra:** Programación 1

## Integrantes

- Agustin Miranda
- Tobias Correa

## Datos de Profesores

**Profesor:** Virginia Cimino
**Tutor:** Alberto Cortez

## Estructura del Proyecto

El proyecto se basa en un modelo de **lista de diccionarios**, donde cada diccionario representa un país. El código está estructurado de forma modular en el archivo `main.py`, dividido en los siguientes bloques:

1.  **Funciones de Utilidad:** Para validación y normalización de entradas.
2.  **Funciones de Gestión de Archivos (CSV):** Para `carga_inicial()` y `actualizar_csv()`.
3.  **Funciones Principales (CRUD):** `agregar_pais()`, `actualizar_pais()`, `buscar_pais()`.
4.  **Funciones de Filtrado:** `filtrar_continente()`, `filtrar_poblacion()`, `filtrar_superficie()`.
5.  **Funciones de Ordenamiento:** `ordenar_paises()` (implementa Bubble Sort ).
6.  **Funciones de Estadísticas:** `pais_mayor_poblacion()`, `promedio()`, `paises_por_continente()`.
7.  **Función Principal (Menú):** `mostrar_menu()` que orquesta el flujo del programa.

## Cómo Ejecutar

1.  Asegúrate de tener Python 3 instalado en tu sistema.
2.  Clona o descarga este repositorio.
3.  Asegúrate de que el archivo `main.py` y `paises.csv` se encuentren en el mismo directorio.
4.  Abre una terminal en ese directorio y ejecuta el siguiente comando:
    python main.py

## Tecnologías Utilizadas

- **Python 3:** Lenguaje principal del proyecto.
- **Módulo `csv`:** Para la lectura y escritura de los datos (persistencia).
- **Módulo `os`:** Para verificar la existencia del archivo `paises.csv`.

## Links

- https://github.com/agus1k/UTN-TUPaD-TPI
- [https://www.youtube.com/watch?v=vRfZqV7UeqA](https://www.youtube.com/watch?v=jfFuIbv3lGc)

# Ejemplos de Entrada y Salida

El programa se maneja a través de un menú numérico.

## Ejemplo de Menú Principal:

    Bienvenido al programa de gestión de paises!
    Elija su opción:
    1. Agregar país
    2. Actualizar datos de un país
    3. Buscar un país
    4. Filtrar países
    5. Ordenar países
    6. Mostrar estadísticas
    7. Salir

## Ejemplo de Flujo (Filtrar países):

### Entrada de Usuario: 4

## Salida del Programa (Sub-menú):

```
Ingrese por que criterio desea filtrar (C - Continente / P - Población / S - Superficie):
Entrada de Usuario: C
```

## Salida del Programa:

```
Ingrese el continente por el cual desea filtrar:
```

### Entrada de Usuario: América

## Salida del Programa (Resultados):

```Estos son los países del continente América:
- Argentina | Población: 45376763 | Superficie: 2780400 | Continente: América
- Bolivia | Población: 11673029 | Superficie: 1098581 | Continente: América
- Uruguay | Población: 3426260 | Superficie: 176215 | Continente: América
```
