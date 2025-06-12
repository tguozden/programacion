<!-- #parcial -->
## 1
(4 puntos)

Construya el diccionario ascii de las letras minúsculas, sabiendo que el código de la letra 'a' es 97 y que son 26 letras.

Recuerde que el caracter asociado a un código ascii se obtiene con la función `char()`:

`char(97) = 'a'`

Utilice diccionarios por comprensión para construirlo, por ejemplo:
`{i:i*10 for i in range(4)}`
retorna el diccionario 
`{0:0, 1:10, 2:20, 3:30}`

## 2
(4 puntos)

Encripta palabra: se quiere ocultar el texto de un determinado string escrito en letras alfabéticas minúsculas. Para ello se tiene un diccionario con los caracteres como clave y el código ascii como valor (como en el punto de arriba). Itere sobre la palabra utilizando listas por comprensión, generando una lista de caracteres nuevos en la que cada caracter se corre ***n*** lugares en la tabla ascii.

```python
def encripta(clave:str, key:int)->str:
   # su código
```



## 3
(2 puntos)

Interprete el siguiente código y deduzca qué se imprimirá en pantalla:
```python
texto = 'abcdef'
def letra(texto, n):
    lista = [j for i,j in enumerate(texto) if i%3 == n]
    return ''.join(lista)

lista = [''.join(i) for i in zip(letra(texto, 2),
                                 letra(texto, 1),
                                 letra(texto, 0))]
print(''.join(lista))
```