import numpy as np
from scipy.io.wavfile import write

def freqNotas(octava):
    # Frecuencia del La en la octava 0
    fLa0 = 27.5
    
    # Frecuencia del La en la octava de interes
    fLa = fLa0 * 2**(octava)
    
    # Frecuencias de las demas notas
    fNotas = np.zeros(12)
    
    # Cargo el La donde corresponde
    fNotas[9] = fLa
    
    # Calculo las demas
    for k in range(1,10):
        fNotas[9 - k] = fNotas[9 - k + 1] /(2**(1/12)) 
        
    for k in range(1,3):
        fNotas[9 + k] = fNotas[9 + k - 1] * (2**(1/12)) 
    
    return fNotas

# Frecuencia de muestreo
fs = 44100
Ts = 1/fs

# Frecuencias de las notas para una octava particular
fNotas = freqNotas(4)

# Duracion de cada nota
tNota = 0.8

# Cantidad de Notas
N = fNotas.size 

# Vector de tiempos por cada nota
t = np.arange(0,tNota,Ts)

# Generacion del vector de datos (primer nota)
data = 0.5*np.sin(2*np.pi*fNotas[0]*t)

# Agregado de las demas notas al vector
for k in range(1,N):
    data = np.concatenate((data,(0.5*np.sin(2*np.pi*fNotas[k]*t))),0)

# Conversion del resultado a entero.
data2 = np.int16(data * 32767)

# Generacion del archivo .wav
write('escalaNotas.wav', fs, data2)