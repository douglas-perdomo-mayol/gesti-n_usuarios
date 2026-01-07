def registrar_usuario(nombre: str, edad: int) -> tuple:
    if not nombre:
        raise ValueError('El nombre no puede estar vacío.')
    if edad < 0:
        raise ValueError('La edad no puede ser negativa.')
    return nombre, edad

def es_mayor_de_edad(usuario: tuple) -> bool:
    return usuario[1] >= 21

def filtrar_mayores(usuarios: list) -> list:
    return [usuario for usuario in usuarios if es_mayor_de_edad(usuario)]
