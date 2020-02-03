import re

def contador_palabras(text):
    contador = dict()

    text2 = text.lower()

    objetos = re.findall(r'[\w]+',text2)
    print("\n\n",objetos)

    for indice in objetos:
        if indice in contador:
            contador[indice] +=1
        else:
            contador[indice] = 1
    return contador


def lectura():
    documentos = []
    with open("corpus.txt","r") as lec:
        for lineas, texto in enumerate(lec):
            documentos.append(texto)
        contado = contador_palabras(texto)
        print(contado)
    
    return documentos



if __name__ == "__main__":
    print(lectura())

