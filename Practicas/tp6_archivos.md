##

## 1) Función lee archivo
Escriba una función para cargar la matriz de datos almacenada en un archivo con valores separados por coma del estilo:

```csv
12.1, 123.3, 3
12.5, 333.1, 32.90
...
```
y devuelva una lista de listas con los renglones como listas anidadas.
`[[12.1, 123.3, 3],[12.5, 333.1, 32.90],..]`

Utilice el método *split* para separar por comas y el método *replace* para quitar espacios, tabuladores y retornos de carro.

Convierta cada valor a enteros si fuera posible, o a números de punto flotante en su defecto.

Utilice manejo de errores en la apertura del archivo y en la conversión a números. Chequee que todos los renglones tienen la misma cantidad de columnas.

La función devolverá la lista e imprimirá cuántos renglones y columnas leyó.

Prototipo:
```python
def lee_archivo(file:str) -> list[list]:
    #su código aquí
```

## 2) Función guarda archivo

Genere la función inversa a la anterior: dada una lista de listas guarde los datos en un archivo. Chequee las dimensiones e imprima. Use manejo de errores donde sea necesario.

Prototipo:
```python
def guarda_archivo(file:list[list]) -> None:
    #su código aquí
```

## 3) Función traspone datos
Implemente la siguiente función. Chequee que las listas anidadas sean todas del mismo tamaño. Utilice manejo de errores para chequear el tipo de datos.
```python
def traspone_lista(datos:list[list])->None:
    ```intercambia renglones y columnas
    de la matriz almacenada en datos.
    ```
```

## 4) Función reacomoda datos (reshape)

Dada una matriz de n filas y m columnas acomoda todos los datos en una sola lista y luego los reacomoda en una matriz de j filas y k columnas, donde j*k=n*m
```python
def reshape_lista(datos:list[list], N:int, M:int)->None:
    # su código
```




## 4) Estudie un caso particular

En el archivo *tp6_eje4.csv* hay una matriz de datos. Cargue los datos y estudie los mismos:
- Enuentre máximo y mínimo
- Calcule promedio y desvío estándar
- Calcule la moda
- Elabore un histograma sencillo de los enteros comprendidos entre el mínimo y el máximo, graficando la barra con algún símbolo de la siguiente manera:

```
min: **
   : ****
   : *****
   : ****
   : *******
   : ***********
   : ****
   : **
   : *
   : 
max: *

```
