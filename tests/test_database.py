import unittest
from src.database__init__ import DataBase

class TestDataBase(unittest.TestCase):

    def setUp(self):
        # Base de datos en memoria
        self.db = DataBase()

    
    def test_insertar_usuario(self):
        self.db.insertar_usuario('Luis', 30, 'Usuario')
        mayores = self.db.obtener_mayores()
        self.assertEqual(len(mayores), 1)
    
    def test_actualizar_usuario(self):
        self.db.insertar_usuario('Lucas', 21, 'Usuario')
        self.db.actualizar_usuario('Lucas', 'Pedro', 22)
        mayores = self.db.obtener_mayores()
        self.assertEqual(len(mayores), 1)

    def test_elminar_usuario(self):
        self.db.insertar_usuario('Juan', 40, 'Usuario')
        self.db.eliminar_usuario('Juan')
        mayores = self.db.obtener_mayores()
        self.assertEqual(len(mayores), 0)

if __name__ == '__main__':
    unittest.main()