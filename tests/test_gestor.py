import unittest
from src.gestor import GestorUsuario
from src.database__init__ import DataBase

class TestGestorUsuario(unittest.TestCase):

    def setUp(self):
        self.db = DataBase()
        self.gestor = GestorUsuario()
        self.gestor.db.nombre_db = ':memory:'
        self.gestor.db._crear_tabla()

    def test_registro_y_consulta(self):
        self.gestor.registrar_usuario('Carlos', 28)
        mayores = self.gestor.obtener_mayores()
        self.assertEqual(len(mayores), 1)


if __name__ == '__main__':
    unittest.main()