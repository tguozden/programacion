# Trabajo Práctico 4: Funciones en Python

## Notas
- Cada función debe incluir un docstring que explique su propósito
- Probar cada función con diferentes argumentos para verificar su comportamiento
- Utilizar valores por defecto cuando sea apropiado, y parámetros posicionales, nombrados y valores por defecto donde corresponda.

---
## Ejercicios

### 1. Función de saludo básico
Crear una función `saludar()` que acepte un nombre como parámetro (con valor por defecto "Usuario") e imprima un saludo personalizado. Demostrar llamadas con 3 argumentos distintos: posicionales, nombrados y usando el valor por defecto. Incluir validación de tipo para que el nombre sea string.


### 2. Función para cálculo de área de triángulo
Convertir el ejercicio de cálculo de área de triángulo del TP1 en una función que reciba base y altura, y retorne el área calculada. Validar que base y altura sean mayores a 0 y numéricos.

### 3. Función con argumentos variables
Crear una función `crear_lista()` que acepte cualquier número de argumentos y los devuelva como lista. Probar con diferentes cantidades de argumentos. Añadir un parámetro ordenar=False como opción para retornar la lista ordenada si se desea.

### 4. Función con parámetros nombrados
Convertir el conversor de temperaturas del TP1 en una función que acepte exclusivamente Celsius o Fahrenheit (usando parámetros nombrados) y devuelva la conversión correspondiente. Validar que se pase uno solo de los parámetros (no ambos o ninguno).
```python
# Ejemplo:
print(convertir_temperatura(celsius=25))  # 77.0
print(convertir_temperatura(fahrenheit=77))  # 25.0
```

### 5. Función para manejar listas
Desarrollar una función `procesar_lista()` que realice diferentes operaciones sobre una lista (mostrar, invertir, sumar) según un parámetro de acción. Incluir un caso por defecto con `pass`. Expandir acciones disponibles: por ejemplo, eliminar duplicados, contar elementos.

Usar match-case (Python 3.10+) si es posible.

```python
# Ejemplo:
procesar_lista([1, 2, 3], 'invertir')  # [3, 2, 1]
```
### 6. Función con argumentos posicionales y nombrados
Crear una función para manejar diccionarios que acepte: 
- El diccionario y una acción que puede ser 'alta', 'baja', 'muestra_valor' como parámetros posicionales
- Clave y valor como parámetros nombrados obligatorios (usando `*`)

```python
# Ejemplo:
persona = {"nombre": "Ana"}
manejar_diccionario(persona, 'alta', clave='edad', valor=30)
manejar_diccionario(persona, 'muestra_valor', clave='nombre') # Ana
```

### 7. Función para conjuntos
Implementar una función que realice operaciones de conjuntos (unión, intersección, diferencia) según un parámetro de operación. Basarse en el ejercicio de conjuntos del TP3. Incluir validación de tipo para asegurar que ambos argumentos sean conjuntos.

Mostrar visualmente las diferencias entre las operaciones en comentarios o prints.

### 8. Función para verificar tipos
Crear una función que verifique si un valor es de un tipo específico, retornando True o False. Usar `isinstance()` como en el TP2. Permitir una lista o tupla de tipos aceptados, no solo uno.

### 9. Función con parámetros opcionales
Convertir el ejercicio de operaciones numéricas del TP1 en una función que calcule cuadrado, cubo y/o valor absoluto según parámetros opcionales.

### 10. Función para manejo de strings
Desarrollar una función que procese texto de diferentes formas (longitud, invertir, separar palabras) según un parámetro de acción. Incluir sanitización básica (strip, lower).

### 11. Función para manejo de tuplas
Crear una función que devuelva información sobre una tupla (longitud, tipos de elementos, primer y último elemento). Basarse en ejercicios de tuplas del TP3.

### 12. Función integradora
Implementar una función que convierta entre diferentes estructuras de datos (lista, tupla, conjunto, diccionario). 

### 13. Función chequea paréntesis
Implementar función que pida un string y que devuelva bool 
evaluando que todos los paréntesis abiertos se hayan cerrado

```python
#ejemplo:
bienparentado( '((pp)' ) # False
bienparentado( ')(' ) # False
bienparentado( '()' ) # True
```
---
