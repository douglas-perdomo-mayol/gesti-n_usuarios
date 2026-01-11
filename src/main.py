from gestor import GestorUsuario

def main():
    gestor = GestorUsuario() 

    while True:
        print('\n--- Menú ---')
        print('1. Registrar usuario')
        print('2. Registrar administrador')
        print('3. Mostrar mayores de edad')
        print('4. Actualizar edad de usuario')
        print('5. Elimiar usuario')
        print('6. Salir')  
        opcion = input('Seleccione una opción: ')

        if opcion == '1':
            gestor.registrar_usuario(
                nombre = input('Nombre: '),
                edad = int(input('Edad: '))
            )
            print('Usuario registrado correctamente.')

        elif opcion == '2':
            gestor.registrar_usuario(
                nombre = input('Nombre admin: '),
                edad = int(input('Edad: ')),
                admin=True
            )
            print('Usuario Admin registrado correctamente.')
        elif opcion == '3':
            registrado = gestor.obtener_mayores()

            if not registrado:
                print('No hay usuarios registros...')
            else:
                for u in registrado:
                    print(u)
            
        elif opcion == '4':
            nombre = input('Nombre del usuario: ')
            nuevo_nombre = input('Nuevo nombre: ')
            nueva_edad = int(input('Nueva edad: '))
            gestor.actualizar_usuario(nombre, nuevo_nombre, nueva_edad)
                
        
        elif opcion == '5':
            nombre = input('Nombre del usuario a eliminar: ')
            gestor.eliminar_usuario(nombre)

        elif opcion == '6':
            print('Saliendo...')
            break
        
        else:
            print('Opción inválida.')

if __name__ == '__main__':
    main()