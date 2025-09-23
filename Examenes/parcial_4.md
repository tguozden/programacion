# Parcial 18 de septiembre 2025

## 1
Construya una función que reciba un objeto `datetime.date` cualquiera y devuelva una cadena de caracteres con la fecha, usando palabras para el día y el mes: 
`"Jueves 18 de septiembre de 2025"`. Cree el string a partir de listas de días de la semana y meses del año, indexando con el entero que proveen el método `.weewkday()` y el atributo `.month` de los objetos con tipo `datetime.date`

Nota: el método es una función que provee un objeto que realiza una acción determinada, y por eso necesita paréntesis. Atributo es una propiedad del objeto, es decir que está a disposición y no es necesario realizar un cálculo para obtenerlo, por ende no llevan paréntesis.

Si le aprovecha:
```python
dias = ['lunes', 'martes', 'miércoles', 'jueves' 'viernes']  # se puede pasar a mayúscula la primera letra con el método `.capitalize()`
meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
```

## 2
El archivo `dibujame.csv` contiene dos columnas de datos. Escriba un script que levante los datos del archivo, grafique la segunda columna (la de la derecha) en función de la primera y guarde la gráfica en formato PNG
