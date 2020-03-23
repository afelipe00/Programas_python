"""manejo de excepciones
con las palabras clave try y except podemos manejar la ecepciones que puder generar crash en nuestros codigos
es importante tener en cuentas que las ecepciones no debenm ser sileciadas esto se da cuando solo imprimimos en la pantalla
las ececpciones.
"""

def divide_lista(lista,div):
    try:
        return [i/div for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista


lista = list(range(10))
divisor = 0

print(divide_lista(lista,divisor))