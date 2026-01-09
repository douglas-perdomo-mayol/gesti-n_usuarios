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
    
    def actualizar_usuario(self, nombre, nuevo_nombre, nueva_edad):
        self.db.actualizar_edad(nombre, nuevo_nombre, nueva_edad)

    def eliminar_usuario(self, nombre):
        self.db.eliminar_usuario(nombre)