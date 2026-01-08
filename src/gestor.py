from usuario import Usuario

class GestorUsuario:
    def __init__(self):
        self._usuarios = []

    def registrar_usuario(self, nombre: str, edad: int):
        usuario = Usuario(nombre, edad)
        self._usuarios.append(usuario)

    def obtener_mayores(self):
        return [u for u in self._usuarios if u.es_mayor_de_edad()]
    
    def listar_usuario(self):
        return self._usuarios