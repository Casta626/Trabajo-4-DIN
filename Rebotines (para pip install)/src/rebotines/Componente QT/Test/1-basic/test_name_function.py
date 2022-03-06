# Importamos la librería de test unitarios de Python
import unittest
# Importamos la función de formatear nombres
from name_function import formatted_name

# La clase debe heredar de unittest.TestCase para que se ejecuten los tests al iniciarse
class NamesTestCase(unittest.TestCase):
   # Método que comprueba con una entrada de ejemplo el método formatted_name
   def test_first_last_name(self):
       result = formatted_name("pete", "seeger")
       self.assertEqual(result, "Pete Seeger")

# Ejecutamos los tests
if __name__ == '__main__':
    unittest.main()