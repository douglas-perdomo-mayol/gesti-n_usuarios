from gestor import GestorUsuario

def mostrar_menu():
    print('\n--- Menú ---')
    print('1. Registrar usuario')
    print('2. Registrar administrador')
    print('3. Mostrar mayores de edad')
    print('4. Salir')

def main():
    gestor = GestorUsuario()

    while True:
        mostrar_menu()    
        opcion = input('Seleccione una opción: ')

        if opcion == '1':
            nombre = input('Nombre: ')
            edad = int(input('Edad: '))
            gestor.registrar_usuario(nombre, edad)

        elif opcion == '2':
            nombre = input('Nombre admin: ')
            edad = int(input('Edad: '))
            gestor.registrar_usuario(nombre, edad, admin=True, nivel=1)

        elif opcion == '3':
            for usuario in gestor.obtener_mayores():
                print(usuario)

        elif opcion == '4':
            print('Saliendo...')
            break
        
        else:
            print('Opción inválida.')

if __name__ == '__main__':
    main()