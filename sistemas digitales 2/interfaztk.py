#se importan la librerias necesaria para poder correr el codigo
import matplotlib.animation as anim
import matplotlib.pyplot as plt
import serial
import Programas_python.modcsv
import tkinter
from matplotlib import style
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#se declaran la caracteristicas de la ventana
window = Tk()
window.title("grafica analogica")
window.geometry('640x480')
#se agrega el estilo que permite plotear en la ventana
style.use('ggplot')
#se crean los vectores de cada una de las graficas
xar = []
yar = []
yar2 =[]
yar3 =[] 
#se agregan las caracteristicas del plot y los subplots
fig = plt.figure(figsize=(5,4), dpi=100)
a = fig.add_subplot(3,1,1)
a.set_ylim(0,1023)
line, = a.plot(xar,yar,'r')
a2 = fig.add_subplot(3,1,2)
a2.set_ylim(0,2)
line2, = a2.plot(xar,yar2,'r')
a3 = fig.add_subplot(3,1,3)
a3.set_ylim(0,2)
line3, = a3.plot(xar,yar3,'r')
plt.xlabel("Seconds")
plt.ylabel("Variable")
#se crean las caracteristicas de la comunicacion serial
ser = serial.Serial(
    port='COM4',
    baudrate=9600
)
#se inicia la comunicacion serial
ser.isOpen()
#funcion de presionado del boton
def boton(lista):
	Programas_python.modcsv.crear_mod(lista)
#funcion de la ventana
def animate(i):
	#ciclo infinito(permite terminar el proceso de la ventana)
	while True:
		#vector que expresa el timepo
		xar.append(i)
		#lectura del puerto serial
		data = ser.readline()
		#conversion a string
		data = str(data)
		#busqueda de las variables diferenciadoras
		af= data.find('A')
		df= data.find('P')
		inter = data.find('D')
		fin= data.find('T')
		fina= data.find('t')
		#almacenamineto de lo resultados
		datum = data[af+1:fina]
		datum2 = data[df+1:inter]
		datum3 = data[inter+1:fin]
		#impresion en la console de los resultados
		print(data)
		print(datum)
		#se llenan las listas utilizadas para las graficas
		yar.append(int(datum))
		yar2.append(int(datum2))
		yar3.append(int(datum3))
		#Teoricamente guarda el dato enviado por el arduino en yar,'Teoricamente' :v
		line.set_data(xar,yar)
		a.set_xlim(0, i+1)
		line2.set_data(xar,yar2)
		a2.set_xlim(0, i+1)
		line3.set_data(xar,yar3)
		a3.set_xlim(0, i+1)
		if KeyboardInterrupt:
			break
#ploteo de las graficas
plotcanvas = FigureCanvasTkAgg(fig,window)
plotcanvas.get_tk_widget().grid(column=1,row=1)
ani = anim.FuncAnimation(fig, animate, interval=50, blit=False)
#cilo infinito de la ventana
window.mainloop()