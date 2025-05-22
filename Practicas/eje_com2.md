### Problema 1: 

Se quiere leer datos booleanos (True - False, respectivamente
representados como 0 - 1) en tiras de 8 datos; a esto lo llamaremos muestra.
Se desea crear un diccionario en el que la clave es el número de fila leída y el
significado una lista de bool.
    -Con un ciclo iterar las filas de archivo (usar una variable entera para contar
las filas leídas)
    -Dentro del ciclo leer la fila y y convertirla en una lista de bool
    -Definir el par en el diccionario
    -Al final, guardar en un archivo una fila por cada entrada del diccionario,
conteniendo un par (clave, significado).

### Problema 2: 
Se quiere poder saber si hay dos muestras iguales en el
diccionario y solo escribir el archivo resultado si no hay duplicados.
    -Recorrer los valores del diccionario armando una lista con ellos, sacando
los elementos (pop), preguntando si el elemento sacado está en la lista que
queda.

