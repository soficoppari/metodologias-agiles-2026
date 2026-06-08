import unittest
from string_calculator import sumar

class TestStringCalculator(unittest.TestCase):
    def test_cadena_vacia_devuelve_cero(self):
        self.assertEqual(sumar(""), 0)

    def test_un_numero_devuelve_el_mismo_numero(self):
        self.assertEqual(sumar("7"), 7)

    def test_un_numero_devuelve_el_mismo_numero_v2(self):
        self.assertEqual(sumar("9"), 9)

    def test_dos_numeros_devuelve_la_suma(self):
        self.assertEqual(sumar("3,4"), 7)

    def test_dos_numeros_devuelve_la_suma_v2(self):
        self.assertEqual(sumar("7,8"), 15)

    def test_tres_numeros_devuelve_la_suma(self):
        self.assertEqual(sumar("2,3,4"), 9)

    def test_varios_numeros_con_salto_de_linea_devuelve_la_suma(self):
        self.assertEqual(sumar("4,5\n6"), 15)

    def test_varios_numeros_solo_con_salto_de_linea_devuelve_la_suma(self):
        self.assertEqual(sumar("2\n3\n4"), 9)

if __name__ == '__main__':
    unittest.main()
