# Recuperatorio general
## 1) Construya las siguientes funciones 
### i)
```python
def palabra2dict(cadena:string) -> dict:
    '''la función devuelve un diccionario donde
    las claves serán el índice de cada caracter
    y los valores el caracter correspondiente. 
    
    Ejemplo: dict2palabra('abc')
    devolverá {0:'a', 1:'b', 2:'c'}
    '''
```

### ii) 
Construya la función inversa al inciso anterior,  tal que tome el diccionario y devuelva la palabra.

### iii)
Construya la función que permita obtener el índice mínimo de una lista: ` def indemin(lista:list)->int`. Por ejemplo `indemin([10, 11, 12, 3, 14])` devolverá 3.

### iv)
Construya una función `def swapea(lista:list, i:int, j:int)->None` que intercambie los elementos `i` y `j` de `lista`. La función saldrá con un aviso de error si alguno de los índices no es válido (considere el caso mayor o igual a `len(lista)` solamente)

## 2: Interprete la función a continuación

Interprete y muestre la salida en pantalla del siguiente código

```python
def questoyhaciendo(lista:list) -> None:
    for i in range(len(lista)):
        imin = i + indemin(lista[i:])
        swapea(lista, i, imin)
        print(lista, i , imin)

lista = [5, 2, 7, 3]
queestoyhaciendo(lista)
print("la lista quedó así:", lista)

```
Las funciones swapea e indemin están explicadas en el punto 1).






