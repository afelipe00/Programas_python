"""basses y test de debug python
programa para entender como hacer testing de los bugs
"""
#pruebas de caja negra
#no conocemos la implementacion
#se basa en la especificaion de la funcion o el programa
#prueba inputs y valida outputs
#unit testing: prueban funcion por funcion viendo que el codigo en cada modulo funcione
#integration testing: es ver que todos los modulos funcionen entre si

import unittest

def suma(num1,num2):
    return abs(num1) + num2

class Cajanegratest(unittest.TestCase):

    def test_suma_positivos(self):
        num_1 = 10
        num_2 = 5

        resultado =  suma(num_1,num_2)

        self.assertEqual(resultado, 15)
    
    def test_suma_negativos(self):
        num_1 = -10
        num_2 = -7

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, -17) 

if __name__ == "__main__":
    unittest.main()

