# (TPI Programación 1)
El objetivo principal de este trabajo practico integrar es aplicar los conocimientos fundamentales de Python para desarrollar un sistema de consola capaz de gestionar un conjunto de datos de países, implementando funcionalidades de filtrado, ordenamiento y cálculo de estadísticas.
## Gestión de Datos de Países en Python 
## Características Principales

El sistema permite gestionar un archivo `paises.csv` a través de un menú interactivo en la consola. Las funcionalidades implementadas son:

* **1. Agregar país:** Permite añadir un nuevo país al registro solicitando nombre, población, superficie y continente.
* **2. Actualizar datos de un país:** Permite buscar un país por nombre y modificar su población o superficie.
* **3. Buscar un país:** Realiza una búsqueda por coincidencias en el nombre del país y muestra sus datos.
* **4. Filtrar países:** Ofrece sub-menús para filtrar el conjunto de datos por:
    * Continente
    * Rango de población (mínimo y máximo)
    * Rango de superficie (mínimo y máximo)
* **5. Ordenar países:** Muestra la lista de países ordenada según el criterio seleccionado:
    * Nombre (alfabético)
    * Población (ascendente)
    * Superficie (ascendente o descendente)
* **6. Mostrar estadísticas:** Calcula y muestra las siguientes métricas sobre el conjunto de datos:
    * País con mayor población
    * País con menor población
    * Promedio de población
    * Promedio de superficie
    * Cantidad de países por continente

## Tecnologías Utilizadas

* **Python 3:** Lenguaje principal del proyecto.
* **Módulo `csv`:** Para la lectura y escritura de los datos (persistencia).
* **Módulo `os`:** Para verificar la existencia del archivo `paises.csv`.

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
