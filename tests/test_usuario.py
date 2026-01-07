import unittest
from src.usuario import registrar_usuario, filtrar_mayores

class testUsuario(unittest.TestCase):
    def test_registro_valido(self):
        self.assertEqual(registrar_usuario('Mario', 30), ('Luis', 30))
    
    def test_nombre_vacio(self):
        with self.assertRaises(ValueError):
            registrar_usuario('', 20)

    def test_edad_negativa(self):
        with self.assertRaises(ValueError):
            registrar_usuario('Lucas', -1)

    def test_filtrar_mayores(self):
        usuarios = [('Juan', 30), ('Marcos', 18), ('Douglas', 21)]
        mayores = filtrar_mayores(usuarios)
        self.assertEqual(mayores, [('Juan', 30), ('Douglas', 21)])

if __name__ == '__main__':
    unittest.main()