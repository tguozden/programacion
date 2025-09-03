def suma(a, b):
    return a + b

def mult(a, b):
    return a*b

print('esto lo hago cuando importo el módulo')
print('en este caso __name__ toma el valor: ', __name__)

if __name__ == '__main__':
	print('funcion principal', suma(1,1))
