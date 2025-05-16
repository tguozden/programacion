## Tentativo parcial
La función *ord()* toma un caracter y devuelve el entero ascii corresondiente
```python
string = "AZaz"
ascii_values = [ord(char) for char in string]
print(f"The ASCII values of '{string}'\nare {ascii_values}")
```
Las letras minúsculas van del 97 al 122 incluido y las mayúsculas del 65 al 90 incluido. De manera inversa, la función *chr()* toma un entero y devuelve un caracter según el código ascii. Podemos entonces pasar una letra mayúscula a minúscula sumando 32 al código ascii correspondiente:
```python
chr(ord('A')+32)
```
o restando para pasar a minúscula.

### Consigna:
Construir la siguiente función:

    cambia_tipo(cadena: str, /) -> str
        Dada una cadena de caracteres cambia las 
        letras que están mayúsculas a minúsculas y 
        viceversa, y deja como están las que no entran 
        en estas categorías.

Por ejemplo:
```python
cambia_tipo('Hola Mundo!') 
#  ->devuelve 'hOLA mUNDO!'
```


Nota: los caracteres son inmutables (hasheables), con lo cual no puede anexarse más letras. Pero sí puede crear una nueva cadena sumando cadenas:

```python
cadena = 'éxitos'
cadena += '!'
print(cadena) 
# -> 'éxitos!'
```

