import unittest
from src.usuario import Usuario

class TestUsuario(unittest.TestCase):

    def test_usuario_valido(self):
        u = Usuario('Lucas', 25)
        self.assertTrue(u.es_mayor_de_edad())

    def test_usuario_menor(self):
        u = Usuario('Juan', 18)
        self.assertFalse(u.es_mayor_de_edad())

    def test_nombre_vacio(self):
        with self.assertRaises(ValueError):
            Usuario('', 20)

    def test_edad_negativa(self):
        with self.assertRaises(ValueError):
            Usuario('Luis', -1)

if __name__ == '__main__':
    unittest.main()