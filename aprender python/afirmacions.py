"""
la palabra clave para las afirnmaciones es assert y lo que hace es
que verifica que la condicion que uno genera a la hora de hacer una operacion
se cumpla
"""

def recibir_string(lista_de_palabras):
    primera_letra = []

    for palabra in lista_de_palabras:
        assert type(palabra) == str , f'{palabra}no es una palabra'
        assert len(palabra) > 0 , f'no se admiten espacion vacios'

        primera_letra.append(palabra[0])
    
    return primera_letra

if __name__ == '__main__':
    print(recibir_string(['palabra',]))
    print(recibir_string(['',]))#error generado segun assert de vacio
    print(recibir_string([1,]))##error generado segun assert de str