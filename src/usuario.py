class Usuario:
    def __init__(self, nombre: str, edad: int):
        self.__nombre = nombre
        self.__edad = edad
        self.__validar()

    def __validar(self):
        if not self.__nombre:
            raise ValueError('EL nombre no puede estar vacío.')
        if self.__edad < 0:
            raise ValueError('La edad no puede ser negativa.')
        
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def edad(self):
        return self.__edad
    
    def es_mayor_de_edad(self) -> bool:
        return self.__edad >= 21
    
    def tipo(self):
        return 'Usuario'
    
    def __str__(self):
        return f'{self.tipo()}: {self.__nombre} ({self.__edad})'
    
class UsuarioAdmin(Usuario):
    def __init__(self, nombre: str, edad: int, nivel: int):
        self._nivel = nivel
        super().__init__(nombre, edad)

    def tipo(self):
        return 'Administrador'
    
    def es_mayor_de_edad(self):
        return True #Polimorfismo: redefine comportamiento
    