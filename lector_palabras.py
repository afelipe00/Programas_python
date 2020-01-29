import re


def lectura():
    with open("C:\Users\Felipe Diaz\Documents\GitHub\Programas_python\corpus.txt","r") as lec:
        text = lec.readline()
        contador = count_words(text)



if __name__ == "__main__":
    lectura()