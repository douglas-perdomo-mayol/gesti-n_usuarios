from gestor import GestorUsuario

def main():
    gestor = GestorUsuario() 

    while True:
        print('\n--- Menú ---')
        print('1. Registrar usuario')
        print('2. Registrar administrador')
        print('3. Mostrar mayores de edad')
        print('4. Salir')  
        opcion = input('Seleccione una opción: ')

        if opcion == '1':
            gestor.registrar_usuario(
                nombre = input('Nombre: '),
                edad = int(input('Edad: '))
            )

        elif opcion == '2':
            gestor.registrar_usuario(
                nombre = input('Nombre admin: '),
                edad = int(input('Edad: ')),
                admin=True
            )
            
        elif opcion == '3':
            for u in gestor.obtener_mayores():
                print(u)

        elif opcion == '4':
            print('Saliendo...')
            break
        
        else:
            print('Opción inválida.')

if __name__ == '__main__':
    main()