# Opciones para elegir como proyecto final de la materia.

Nos quedan más de 10 clases para trabajar en un proyecto a elección. La idea sería trabajar en grupos de a dos alumnos. Las clases presenciales las usaremos para mostrar temas nuevos y para que trabajen en los proyectos.

La idea es trabajar en un repositorio, `README.md` donde quede la documentación de lo que se hizo.

Se puede también crear un sitio web de acceso público, insertando figuras interactivas a partir de bibliotecas como `plotly`

## Ideas
### 1) Análisis de datos personales como puede ser Spotify, Youtube o el uso del teléfono.

Posibles tareas:
- Explorar las posibles fuentes de datos. Ver formato (csv, json, txt?), volumen, categorización y luego decidir si son adecuados.
- Pandas: cargar los archivos JSON/CSV que exportas de estas plataformas. Completar con los DataFrames adecuadamente, ordenando índices y columnas, evaluando la posibilidad de usar multi-índices si fuera necesario y dando formato adecuado a las fechas.
- Posibles preguntas: Artistas/temas más escuchados, horarios del día con mayor uso, hábitos semanales, descargar lista de favoritos, etc.
- Posibles gráficos: barras para artistas más escuchados, gráficos de línea, gráficos de torta (distribución de géneros musicales)

### 2) Análisis de datos de acceso público, como por ejemplo datos climáticos, financieros o deportes.

Posibles tareas:

- descargar datos, por ejemplo de https://www.kaggle.com/datasets/samoilovmikhail/ocean-buoys-data-1980-2025
- Pandas: cargar los archivos JSON/CSV que exportas de estas plataformas. Completar con los DataFrames adecuadamente, ordenando índices y columnas, evaluando la posibilidad de usar multi-índices si fuera necesario y dando formato adecuado a las fechas.
- discutir distintas ideas sobre qué presentar de los datos, evolución en escalas temporales adecuadas, gráficos de mapas (ej.: librería `cartopy`), gráficos burbuja, etc

### 3) Visualización de datos meteorológicos
También orientado al tratamiento y visualización de datos, la idea es mostrar variables meteorológicas
en la web. Como punto de partida puedo darles permiso para usar los datos que se muestran en la siguiente página: https://unrnmeteo.github.io/meteo/historial.html .
Ideas para trabajar: agregar visualizaciones como por ejemplo gráficos de temperatura en función de la altura, rosas de viento o mostrando datos online de algún broker mqtt implementando un websocket en javascript.

-----------
---------
En una línea distinta a la visualización y tratamiento de datos (y mayor dificultad) las siguientes propuestas consisten en armar versiones simplificadas de juegos. La idea es trabajar en una interfaz gráfica, que puede ser PyQt. La programación de los juegos puede requier usar más intensivamente conceptos de programación orientada a objetos, que no hemos visto y que yo tampoco soy experto. Pero si se animan pueden intentar aunque sea la versión más simplificada de algún juego que conozcan. 

Aquí las siguientes sugerencias:


### 4) Juegos: versión simplificada de un tetris
Para simplificarlo usaremos bloques cuadrados solamente, y el usuario puede elegir adónde ubicarlos.

### 5) Juegos: versión simplificada del *snake*
Juego de la viborita, con tamaño constante condiciones de contorno periódicas y sin comida ni otros agregados.

### 6) Juegos: buscaminas
A diferencia de los anteriores en este caso el juego es estático, y se espera la acción del jugador para continuar. Dificultad media/alta

Pasos a resolver para aproximar al problema:
- graficar una "pared de cerámicos"
- clickear en uno de los cerámicos y que cambie de color

----------------
------------

### 7) Otras propuestas?