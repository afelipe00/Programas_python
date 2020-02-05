import serial
import modcsv
import grafica

ser = serial.Serial(
    port = 'COM4', 
    baudrate = 9600
)

line = []
data = 0

while True:
    if ser.inWaiting()>0:
        tx = ['1','2','3','4','5','6']
        for i in range(5):
            ser.write(tx[i].encode())
        lec = str(ser.readline())
        data = lec.find('A')
        if data != -1:
            ini = lec.find('A')
            fin = lec.find('T')
            analogica = lec[ini+1:fin]
            analogica = int(analogica)
            line.append(analogica)
        else:
            ini = lec.find('P')
            fin = lec.find('T')
            digital = lec[ini+1:fin]
            digital = str(digital)
        if digital == '01':
            ser.close()
            break
    print("finalizado.")
    print(len(line))
    print(line)
grafica.funcion(line)
print("enviando a csv..")
modcsv.crear_mod(line)





