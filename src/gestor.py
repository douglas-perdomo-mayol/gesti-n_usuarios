from database import DataBase
from usuario import Usuario, UsuarioAdmin

class GestorUsuario:
    def __init__(self):
        self._usuarios = []
        self.db = DataBase()

    def registrar_usuario(self, nombre, edad, admin=False):
        tipo = 'Administrador' if admin else 'Usuario'
        self.db.insertar_usuario(nombre, edad, tipo)        
    
    def obtener_mayores(self):
        filas = self.db.obtener_mayores()
        usuarios = []

        for id, nombre, edad, tipo in filas:
            if tipo == 'Administrador':
                usuarios.append(UsuarioAdmin(id, nombre, edad, tipo))
            else:
                usuarios.append(Usuario(id, nombre, edad))
        return usuarios
    
    def actualizar_usuario(self, nombre, nuevo_nombre, nueva_edad):
        actualizar = self.db.actualizar_usuario(nombre, nuevo_nombre, nueva_edad)

        if not actualizar:
            print(f'Advertencia: {nombre} no existe.')
        else:
            print('Usuario actualizado correctamente.')

    def eliminar_usuario(self, nombre):
        eliminar = self.db.eliminar_usuario(nombre)

        if not eliminar:
            print(f'Advertencia: {nombre} no está registrado.')
        else:
            print('Usuario elimiado correctamente.')