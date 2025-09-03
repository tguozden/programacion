from matplotlib import pyplot as plt
def carga_csv(namefile:str)->list[list]:
    try:
        with open(namefile, 'r') as file:
            datos = []
            for row in file:
                if row[0] == '#': continue
                fila = row[:-1].split(',')
                for i in range(len(fila)):
                    cadena = fila[i]
                    if cadena.isdigit():
                        fila[i] = int(fila[i])
                    else:
                        fila[i] = float(fila[i])
                datos.append(fila)
        return datos
    except Exception as e:
        print('salió con error', e)
def traspone(datos:list[list])->list[list]:
    traspuesta = []
    for fila in zip(*datos):
        traspuesta.append(list(fila))
    return traspuesta

datos = carga_csv('/home/atom/Downloads/co2_mm_gl.csv')
datos_t = traspone(datos)

plt.plot(datos_t[2],datos_t[3])
plt.show()


