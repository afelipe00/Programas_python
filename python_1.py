#programa en el cual se va a aprender lo basico de python

#!/usr/bin/env/python    se crea en entorno en el cual se va a ejecutar (no es necesario colocarlo) 
#_*_ coding: utf8 _*_      se indica la codificacion que se va a usar (util para las tildes etc.)

#imprimir en pantalla (clasico hola mundo)
print("!hola mundo!")

#TIPOS DE DATOS (variables)
#string
palabra = "hola usuario" # se declara la variable string
print(type(palabra)) # el comando type sirve para poder saber que tipo de variable se esta usando 
#entero
entero = 10 # se declara la variable entera
print(type(entero))
#flotante
flotante = 1.2 # se declara la variable flotante
print(type(flotante))
#booleano
bandera = True
print(type(bandera))

#OPERADORES
#comparadores (relacionan o comparan dos variables)
# = asignacion
# == igualdad
# != distintos
# < menor que 
# > mayor que
# <= menor igual que
# >= mayor igual que
#logicos (devuelven un valor booleano)
# and y
# or o
# not no
#aritmetico (operaciones matematicas)
# + suma
# - resta
# * multiplicacion
# / division
# ** exponente
# // division entera
# % modulo o residuo
#booleanos
# bool() funciona para saber el valor booleano de un dato ( vacio o None = false, lleno = true)
print(bool(0)) # imprime falso dado que el 0 se interpreta como vacio
print(bool(None)) # imprime falso (en python None = null)
print(bool(1)) # imprime true dado que ya es un valor "lleno"
#operaciones con cadenas de texto
saludo = "hola"
persona = "diego"
print(saludo * 3)
print(saludo + persona)
print(saludo < persona) #orden alfabetico
añadir = "hey"
añadir += " "
añadir += "buena"
print(añadir) #concatenarle al texto
print(len(añadir))#imprimir el tamaño de la cadena de texto
print(saludo.find("o"))#encuentra la cadena de texto o caracter (devuelve la posicion de la variable encontrada)
saludo = "HOLA MUNDO"
print(saludo.lower())#convertir en minusculas
saludo = "hola mundo"
print(saludo.upper())#convertir en mayusculas
saludo = "HOLA MUNDO"
print(saludo.replace("L","m"))#remplazar 
print('Hola\tHola\tHola\nMundo')#espacio y enter
print("hola{:>10}".format("mundo"))#espacios establecidos (setw)

#ENTRADA DE DATOS
name = input("ingrese el nombre: ")
edad = int(input("ingrese su edad: "))#se recibe una variable como entero
print("hola {}, su edad es {}".format(name,edad),"\n")#format reemplaza en la llaves la variable seleccionada

#SENTENCIAS
#condicionales
a = True
b = False
if a == True and b == True: #si se cumple
    print("verdadero")
elif a == False and b == False: # si no, si se cumple
    print("falso")
else: # si no se cumplen
    print("none")
#ciclos
#while
limit = int (input("ingrese el limite: "))
i = 0
while i < limit: 
    print(i,": lets go")
    i+=1
#for
for i in range(0,limit):
    print(i,": for lets go")

#ESTRUCTURAS DE DATOS
#listas
lista = list() #forma 1 de declarar una lista
lista2 = [] #forma 2 de declarar una lista
print(type(lista))
lista = ['a','b','d','f','e','e','r',12,'e']
#formas de imprimir una lista
print(lista)
i=0
for i in lista:
    print(i)
    print("posicion", lista.index(i))






