from usuario import registrar_usuario, filtrar_mayores

usuarios  = []

def mostrar_menu():
    print('\n--- Menú ---')
    print('1. Registrar usuario')
    print('2. Mostrar mayores de edad')
    print('3. Salir')

def main():
    while True:
        mostrar_menu()
        opcion = input('Seleccione una opción: ')

        if opcion == '1':
            try:
                nombre = input('Nombre: ')
                edad = int(input('Edad: '))
                usuario = registrar_usuario(nombre, edad)
                usuarios.append(usuario)
                print('Usuario registrado correctamente.')
            except ValueError as e:
                print('Error:', e)
            
        elif opcion == '2':
            mayores = filtrar_mayores(usuarios)
            print('\nUsuarios mayores de edad:')
            for nombre, edad in mayores:
                print(f'- {nombre} ({edad})')
        
        elif opcion == '3':
            print('Saliendo del sistema...')
            break

        else:
            print('Opción no válida.')

if __name__ == '__main__':
    main()