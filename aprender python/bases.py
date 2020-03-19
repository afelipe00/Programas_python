#operaciones con strings
my_str = 'felipe'
print(len(my_str))#retorna el tamano del str
print(my_str[0])#retorna el caracter en la posicion 0
print(my_str[:4])#retorna los caracteres desde el principio hasta la posicon 4
print(my_str[2:])#retorna los caracteres desde la posicion 2 hasta el final
print(my_str[::2])#retorna todos los carcteres saltando cada 2 pasos
print('hola yo soy '+my_str)#el operador + concatena los strings
print(f'hola yo soy {my_str}')#es el operador formato que nos permite dar formatos a los diferentes string
print(f' hola yo soy {my_str}'*10)#el op * repite el string el numero de veces por el que se multiplica

"""
las cadenas son inmutables!!, cuandos se concatenan o se realizan operaciones con los strings
realmente se crea otra cadena que ocupa otro espacio en la direccion de memoria
"""
#recibir datos por el teclado
nombre = input('cual es tu nombre: ')
print('tu nombre es ', nombre)
numero = input('ingrese un numero: ')
print('el numero es', numero)
print(type(numero))
"""la funcion input recibe los datos como str, para convertirlos se deve hacer:"""
entero = int(input('ingrese el entero: '))
print('el entero es:', entero)
print(type(entero))

#otros operadores
print(2==3)
print(2!=3)
print(2<=3)
print(2>=3)
print(True and True)
print(False or True)
print(not True)



