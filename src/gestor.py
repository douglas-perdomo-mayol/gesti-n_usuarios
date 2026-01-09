from database import DataBase

class GestorUsuario:
    def __init__(self):
        self._usuarios = []
        self.db = DataBase()

    def registrar_usuario(self, nombre, edad, admin=False):
        tipo = 'Administrador' if admin else 'Usuario'
        self.db.insertar_usuario(nombre, edad, tipo)        
    
    def obtener_mayores(self):
        return self.db.obtener_mayores()