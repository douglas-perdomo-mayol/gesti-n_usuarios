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
    
    def __str__(self):
        return f'{self.__nombre} ({self.__edad})'