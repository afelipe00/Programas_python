import csv

def crear_mod(data):
    myfile = open('documento.csv','w',newline='')
    data = map(int, data)
    file = [data]
    arch = csv.writer(myfile)
    arch.writerow(['Potenciometro'])
    arch.writerows(zip(*file))
    print("Archivo creado")  
