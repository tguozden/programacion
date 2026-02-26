## Final Programación 1 
### 2da mesa febrero 2026 - libre


1. Dé una función que tome una lista de elementos, identifique cuáles son únicos y cuente cuántas veces aparece cada elemento en la lista. La función devolverá un diccionario en donde las claves serán los elementos (sin repetir) y los valores será un entero que indique las veces que el elemento esté repetido en la lista.

Escriba otra función que, aprovechando la anterior, imprima un histograma de frecuencias de aparición de cada elemento. Es decir, si el elemento 'a' aparece 3 veces imprime 3 asteriscos.

A modo de ejemplo la lista `milista = ['a', 'c', 'a', 'a', 'b', 'c']` el resultado de llamar `imprime_histo(milista)` será:
```
a	: ***
c	: **
b	: *
```
(no importa el orden)

1. Dada una lista de enteros **list_in**, deseamos implementar una función que retorna una lista **list_out** de tuplas, en donde cada tupla indica el índice donde comienza cada escalera (0 para el primero) y cuántos elementos tiene. 

Llamamos escalera ascente a una secuencia creciente de 2 o más enteros consecutivos, como por ejemplo `[1, 2, 3]`
Ejemplo de salida de la función:
```python
list_in = [1, 4, 5, 6, 7, 8, 10, 10, 11]
list_out = [(1,2), (3,3), (7,2)]
```

3. Implementar una función que resuelva el problema de string matching. Esto es: dado dos string `frase` y `palabra` buscar en que posición de `frase` está `palabra`, si es que está. No se pueden usar funcones ni métodos de la clase `str`, como por ejemplo index, find, etc.

4. Escriba una función que tome dos enteros `n` y `m` y devuelva una matriz de *n* filas y *m* columnas, cuyos elementos sean ceros y unos, siguiendo el patrón de blancas y negras de un tablero de ajedrez. Es decir los elementos vecinos por fila o por columna deben ser distintos (como en un tablero de ajedrez). Por ejemplo, si un elemento es 0, sus vecinos horizontales y verticales deben ser 1.
Empiece de tal manera que el elemento de la primera fila y primera columna es cero.


