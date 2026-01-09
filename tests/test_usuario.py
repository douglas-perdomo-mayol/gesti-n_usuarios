import unittest
from src.usuario import Usuario, UsuarioAdmin

class TestUsuario(unittest.TestCase):

    def test_usuario_valido(self):
        u = Usuario("Lucas", 25)
        self.assertTrue(u.es_mayor_de_edad())

    def test_usuario_menor(self):
        u = Usuario("Juan", 18)
        self.assertFalse(u.es_mayor_de_edad())

    def test_nombre_vacio(self):
        with self.assertRaises(ValueError):
            Usuario("", 20)

    def test_edad_negativa(self):
        with self.assertRaises(ValueError):
            Usuario("Luis", -1)


class TestPolimofismo(unittest.TestCase):

    def test_polimorfismo_tipo(self):
        usuarios = [
            Usuario('Juan', 20),
            UsuarioAdmin('Carlos', 17, 1)
        ]

        tipos = [u.tipo() for u in usuarios]
        self.assertEqual(tipos, ['Usuario', 'Administrador'])
    def test_admin_es_mayor(self):
        admin = UsuarioAdmin('Root', 10, 1)
        self.assertEqual(admin.es_mayor_de_edad(), True)



if __name__ == '__main__':
    unittest.main()