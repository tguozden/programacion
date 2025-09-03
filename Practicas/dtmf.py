import numpy as np
from scipy.io.wavfile import write
from matplotlib import pyplot as plt

def freqDtmf(nombre):
    # Frecuencia de las columnas y de las filas
    fColumn = [1209, 1336, 1477]
    fFila = [697, 770, 852, 941] 	

    # Nombres de las teclas
    nombresTeclas = [['1', '2', '3'], ['4','5','6'], ['7','8','9'],['*','0','#']]
    
    freq1 = 0
    freq2 = 0

    for i in range(0,4):
        for j in range(0,3):
            if(nombresTeclas[i][j] == nombre):
                freq1 = fFila[i]
                freq2 = fColumn[j]

    return freq1, freq2



# Frecuencia de muestreo
fs = 44100
Ts = 1/fs

# Numero a discar
numeroDiscar = "15236980"

# Duracion del tono de numero
Tnum = 0.5

# Duracion del silencio 
Tsil = 0.2

# Vector de tiempos por cada tecla y por cada silencio
tNum = np.arange(0,Tnum,Ts)
tSil = np.arange(0,Tsil,Ts)

# Generacion del vector de datos (primer silencio)
data = np.zeros(tSil.shape)

# Agregado de las demas notas al vector
for k in range(0,len(numeroDiscar)):
    f1, f2 = freqDtmf(numeroDiscar[k])
    data = np.concatenate((data,0.5*np.sin(2*np.pi*f1*tNum) + 0.5*np.sin(2*np.pi*f2*tNum)),0)
    data = np.concatenate((data,np.zeros(tSil.shape)),0)                          

# Conversion del resultado a entero.
data2 = np.int16(data * 32767)

# Generacion del archivo .wav
write('discado.wav', fs, data2)

# Grafica total
plt.plot(data)

#  zoom
plt.figure()
plt.plot(data)
plt.xlim(round(Tsil/Ts)-100, round(Tsil/Ts)+1000)