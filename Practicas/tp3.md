# Tuplas, conjuntos y diccionarios

## Ejercicios con Tuplas

Las tuplas son inmutables y útiles para datos que no cambian.
1. Básico: Creación y acceso

    Crea una tupla con los días de la semana. Imprime el primer y último día.

    Intenta modificar un elemento (verifica que falle por inmutabilidad).

2. Desempaquetado

    Dada la tupla ("Ana", 25, "Ingeniera"), desempaqueta los valores en tres variables (nombre, edad, profesión) e imprímelos.

3. Concatenación y repetición

    Combina dos tuplas: (1, 2, 3) y ("a", "b", "c") en una sola.

    Repite la tupla ("Hola",) 3 veces.

4. Búsqueda en tuplas: 

    Dada tupla = (10, 20, 30, 20, 40), cuenta cuántas veces aparece el número 20 de dos maneras, recorriendo la lista y usando el método _.count()_

## Ejercicios con Conjuntos (Sets)

Los conjuntos no permiten duplicados y son ideales para operaciones matemáticas.
1. Básico: Creación y operaciones

    Crea un conjunto __A__ a partir de los elementos de la lista [1, 2, 3, 4] y otro __B__ usando los elementos de la tupla (3, 4, 5, 6)

    Imprime la unión, intersección y diferencia (A - B). Aproveche los métodos de conjuntos

2. Eliminar duplicados

    Dada la lista [1, 2, 2, 3, 4, 4, 4], cree otra lista sin valores duplicados. 

3. Verificar  subconjunto

    Dados C = {1, 2} y D = {1, 2, 3, 4}, verifica si C es subconjunto de D.

4. Diferencia simétrica: _.symmetric_difference()_

    Usando A y B del ejercicio 1, imprime los elementos que están en A o B pero no en ambos.

## Ejercicios con Diccionarios

Los diccionarios almacenan pares clave-valor.

1. Básico: Creación y acceso

    Crea un diccionario persona = {"nombre": "Carlos", "edad": 30, "ciudad": "Madrid"}.

    Imprime el valor de la clave "edad" y añade una nueva clave "profesión".

2. Recorrer diccionario

    Itera sobre el diccionario persona e imprime cada clave y su valor con el formato:
    python

    "clave: nombre, valor: Carlos"

3. Fusión de diccionarios

    Combina dos diccionarios:
    ```python

    dic1 = {"a": 1, "b": 2}
    dic2 = {"b": 3, "c": 4}
    ```

    (Si hay claves repetidas, quédate con el valor de dic2).

4. Diccionario de frecuencias

    Dada la lista ["manzana", "banana", "manzana", "pera", "banana"], crea un diccionario que cuente las ocurrencias de cada palabra.
    
5. Uso de .keys()

    Dado el diccionario productos = {"manzana": 0.5, "banana": 0.3, "pera": 0.4}, imprime todas las claves (nombres de productos) y verifica si "banana" está presente.

6. Uso de _.values()_

    Del mismo diccionario productos, calcula el precio total de todos los productos sumando sus valores.

7. Uso de _.items()_
    Itera sobre el diccionario productos e imprime cada par clave-valor con el formato:
"Producto: manzana, Precio: 0.5".

8. Filtrar claves con _.keys()_

    Crea una lista con las claves del diccionario productos que tengan un precio menor a 0.4.

9. Convertir _.items()_ a lista de tuplas

    Convierte el diccionario productos en una lista de tuplas (clave, valor) y ordénala alfabéticamente por nombre.



## Ejercicios Integrados

Combina múltiples estructuras.
1. Tupla a diccionario

    Convierte la tupla (("nombre", "Luis"), ("edad", 25), ("ciudad", "Lima")) en un diccionario.

2. Lista de diccionarios a conjunto

    Dada una lista de diccionarios como:
    python

    [{"id": 1, "nombre": "Ana"}, {"id": 2, "nombre": "Luis"}, {"id": 1, "nombre": "Ana"}]

    Elimina los diccionarios duplicados (convierte a un conjunto de tuplas).

3. Intersección de valores únicos

    Dadas dos listas [1, 2, 2, 3, 4] y [3, 4, 5, 6], imprime los valores que están en ambas listas (sin duplicados). Usa conjuntos.

4. Diccionario de conteo con _.items()_

    Dada la lista ["a", "b", "a", "c", "b", "a"], crea un diccionario que cuente las ocurrencias de cada letra usando recorriendo el diccionario y usando _.items()_ para imprimir los resultados.

Solución ejemplo (Eje 4 de diccionarios)
```python
lista = ["manzana", "banana", "manzana", "pera", "banana"]
frecuencias = {}

for palabra in lista:
    if palabra in frecuencias:
        frecuencias[palabra] += 1
    else:
        frecuencias[palabra] = 1

print(frecuencias)  # Salida: {"manzana": 2, "banana": 2, "pera": 1}
```
