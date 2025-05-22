# Ejercicios para Practicar `enumerate()` y `zip()` en Python

## Ejercicio 1
    `enumerate()` Básico
 Imprime cada elemento de una lista junto con su índice usando `enumerate()`.
Lista: `frutas = ["manzana", "banana", "naranja"]`

---

## Ejercicio 2
    `enumerate()` con Condicional
 Imprime solo los elementos en posiciones pares (0, 2, 4...) de una lista.
Lista: `colores = ["rojo", "verde", "azul", "amarillo", "negro"]`

---

## Ejercicio 3
    `zip()` Básico
 Combina dos listas en pares `(nombre, edad)` usando `zip()`.
Listas:```python
nombres = ["Ana", "Luis", "Marta"]
edades = [25, 30, 28]
```

---

## Ejercicio 4 
    `zip()` con Tres Iterables

 Combina tres listas (producto, precio, stock) e imprime solo los productos con stock mayor a 0.
Listas:
```python
productos = ["laptop", "mouse", "teclado"]  
precios = [1000, 20, 50]  
stock = [0, 15, 10]  
```
---

## Ejercicio 5
    `enumerate()` + `zip()`

 Dada una lista de estudiantes y sus notas, imprime el número de estudiante (1, 2, 3...) junto con su nombre y nota.
Listas:
```python
estudiantes = ["Carlos", "Ana", "Pedro"]  
notas = [8.5, 9.0, 7.5]  
```

Salida esperada:
```
Estudiante 1: Carlos - Nota: 8.5  
Estudiante 2: Ana - Nota: 9.0  
Estudiante 3: Pedro - Nota: 7.5 
```
---

## Ejercicio 6
    Transposición de Matriz usando `zip()`
 Escribe una función que tome una matriz y devuelva su transpuesta usando `zip(*matriz)`. 

Notas: Una matriz en python puede representarse con una lista de listas. el asterisco * adenlante de la variable en `zip(*matriz)` es para desempaquetar la lista: quitar el primer y último corchete para pasar los elementos que contiene como argumentos.

Matriz de ejemplo:
```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```
La función deberá devolver la matriz: 

```python
[
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
```