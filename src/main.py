from gestor import GestorUsuario

def mostrar_menu():
    print('\n--- Menú ---')
    print('1. Registrar usuario')
    print('2. Mostrar mayores de edad')
    print('3. Salir')

def main():
    gestor = GestorUsuario()

    while True:
        mostrar_menu()    
        opcion = input('Seleccione una opción: ')

        if opcion == '1':
            try:
                nombre = input('Nombre: ')
                edad = int(input('Edad: '))
                gestor.registrar_usuario(nombre, edad)
                print('Usuario registrado.')

            except ValueError as error:
                print('Error:', error)

        elif opcion == '2':
            print('\nUsuarios mayores de edad:')
            for usuario in gestor.obtener_mayores():
                print(usuario)

        elif opcion == '3':
            print('Saliendo...')
            break

        else:
            print('Opción inválida.')

if __name__ == '__main__':
    main()