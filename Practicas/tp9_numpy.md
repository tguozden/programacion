## Práctica 9: Numpy

Péguenle una mirada al [tutorial principiantes](https://numpy.org/doc/stable/user/absolute_beginners.html)

### Repetir ejercicio 4 práctica 6, usando *np.genfromtxt(archivo, delimiter=',')*
Quite la última columna de NaNs.
Observe la cantidad de datos y la estructura de la matriz: cantidad de filas y columnas. ¿Cuál es el data type con que se cargó? Convierta a int32.

Grafique el histograma de los datos con *plt.hist* de matplotlib.

Calcule el promedio de cada columna utilizando *np.mean(mat,axis=0)*
Calcule también el mínimo, máximo, la mediana y la moda de cada columna.


### Ejercicios Intro teleco:

1. Grafique simultáneamente las siguientes señales, cada una en un subplot separado.

- a) 
    - f(t) = sen(2 π t), 
    - g(t) = 5 sen(2 π t)
- b) 
    - f(t) = sen(2 π t), 
    - g(t) = sen(2 π (t − 1))
- c) 
    - f(t) = sen(2 π t), 
    - g(t) = cos(2 π t)
- d) 
    - f(t) = sen(2 π t), 
    - g(t) = − sen(2 π t)
- e) 
    - f(t) = sen(2 π t), 
    - g(t) = sen- (2 π t + π )
- f) 
    - f(t) = sen(2 π t), 
    - g(t) = cos(2 π t − π /2)
- g) 
    - f(t) = sen(2 π t), 
    - g(t) = sen(2 π 10 t)
- h) 
    - f(t) = sen(2 π t), 
    - g(t) = sen(2 π 4 t), 
    - h(t) = f(t) + g(t)
- i) 
    - f(t) = sen(2 π t), 
    - g(t) = sen(2 π 4 t), 
    - h(t) = f(t) g(t)
- j)
    - f(t) = sen(2 π t), 
    - g(t) = sen(2 π 4 t), 
    - h(t) = (1 + 0,2f(t)) g(t), 
    - p(t) = (1 + 0,2f(t))


2. El código Python de *dtmf.py* permite generar una secuencia de tonos con las notas de la escala cromática.
- a) Ejecute el código y analice el resultado.
- b) Analice cómo podría modificar el código para generar una melodía simple.
- c) Si se anima, analice cómo podrían generarse notas con diferente timbre.

3 
El código Python *sinTones.pdf* permite generar el sonido del discado de algún número telefónico particular en el sistema DTMF (siglas en inglés de Dual-Tone Multi-Frequency).

- a) Investigue cómo funciona el sistema DTMF.
- b) Ejecute el código y analice el resultado.
- c) Compare gráficamente las señales de discado para las diferentes teclas.





