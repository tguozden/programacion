# Parcial 18 de septiembre 2025

## 1
Construya una función que reciba una cadena de caracteres con una fecha en el formato: 
`"jueves 18 de septiembre de 2025"`. Trabajando con el string, la función obttendrá los elementos necesarios para construir y devolver un objeto `datetime.date` con la fecha indicada. La función también deberá chequear que el string sea ingresado correctamente, por ejemplo que tenga 6 palabras, etc. Se valorará el uso de excepciones.

Pista: use el método `.split()`

Si le sirve para copiar y pegar:
```python
meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

dias = ['domingo', 'lunes', 'martes', 'miércoles', 'jueves' 'viernes', 'sábado']
```

## 2
El archivo `matricita.csv` contiene 4 columnas de datos con información temporal: año, mes día y hora respectivamente. Obtenga el array unidimensional (o lista si prefiere) con los objetos fecha-hora (*timestamps*), ya sea en formato `datetime.datetime` o en el formato de numpy para este caso.
