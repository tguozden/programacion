# Recuperatorio agosto 2025

## 1) Dados los diccionarios:
```python

# precio por kilo
frutas = {'banana': 2800, 'mandarina': 1500, 'naranja': 1400, ....}
verdura = {'tomate': 2500, 'espinaca': 3500, .....}

# compra realizada en kilos
compra = {'banana': 1, 'naranja': 1.5, 'tomate': 2.25, 'espinaca': .75 .....}

```
### Dé las líneas necesarias para calcular:


1. Cuántos kilos de verdura se compraron
2. Cuántos kilos de fruta se compraron
3. Cuánto se gastó en frutas 
4. Cuánto se gastó en verduras
5. Cuánto se gastó en total.


## 2: Cadenas de caracteres
Cree una función que tome una cadena de caracteres y devuelva el índice que ocupa el caracter con menor código ascii. Recuerde que `ord(c)` devuelve el entero número ascii de la cadena de un carater `c`

## 3: Interprete la función a continuación

Interprete y muestre la salida en pantalla al ejecutar este código

```python
def adivina(lista:list) -> None:
    N = len(lista)
    i = 0
    while(i < N/2):
        aux = lista[i]
        lista [i] = lista[N - 1 - i]
        lista[N - 1 - i] = aux
        i = i + 1
        
lista = [1, 2, 3, 4]
adivina(lista)
print(lista)
```





