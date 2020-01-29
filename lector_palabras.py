import re


def lectura():
    documentos = []
    with open("corpus.txt","r") as lec:
        for lineas, texto in enumerate(lec):
            documentos.append(texto)
    return documentos


if __name__ == "__main__":
    print(lectura())