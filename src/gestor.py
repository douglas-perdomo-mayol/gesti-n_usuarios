import json
from usuario import Usuario, UsuarioAdmin

class GestorUsuario:
    def __init__(self, archivo='usuarios.json'):
        self._usuarios = []
        self._archivo = archivo
        self.cargar()

    def registrar_usuario(self, nombre: str, edad: int, admin=False, nivel=0):
        if admin:
            usuario = UsuarioAdmin(nombre, edad, nivel)
        else:
            usuario = Usuario(nombre, edad)

        self._usuarios.append(usuario)
        self.guardar()
    
    def obtener_mayores(self):
        return [u for u in self._usuarios if u.es_mayor_de_edad()]

    def guardar(self):
        data = []
        for u in self._usuarios:
            data.append({
                'nombre' : u.nombre,
                'edad' : u.edad,
                'tipo' : u.tipo()
            })

        with open(self._archivo, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
    
    def cargar(self):
        try:
            with open(self._archivo, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for u in data:
                    if u['tipo'] == 'Administrador':
                        self._usuarios.append(
                            UsuarioAdmin(u['nombre'], u['edad'], nivel=1)
                        )
                    else:
                        self._usuarios.append(
                            Usuario(u['nombre'], u['edad'])
                        )
        except FileNotFoundError:
            pass

    def listar_usuarios(self):
        return self._usuarios