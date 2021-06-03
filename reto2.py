from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


list_menu = ["1. Cambiar contraseña", "2. Ingresar coordenadas actuales", "3. Ubicar zona wifi más cercana",
             "4. Guardar archivo con ubicación cercana", "5. Actualizar registros de zonas wifi desde archivo",
             "6. Elegir opción de menú favorita", "7. Cerrar sesión"]
counter = 0
while counter < 3:
    print("Elija una opción")
    favorito = int(input(""))
    if favorito == 6:
        counter = 0
        print("Seleccione opción favorita")
        favorita = int(input(""))
        if favorita >= 1 <= 5:
            adivinanza1 = int(input(
                "Para confirmar por favor responda:Me separaron de mi hermano siamés,antes era un ocho y ahora "
                "soy un: "))
            if adivinanza1 == 3:
                adivinanza2 = int(input(
                    "Para confirmar por favor responda:Soy más de uno sin llegar al tres, y llego a cuatro cuando dos "
                    "me des: "))
                if adivinanza2 == 2:
                    eliminado = list_menu.pop(favorita)
                    list_menu.insert(0, eliminado)
                    clear()
                else:
                    print("Error")
            else:
                print("Error")
            print(list_menu)
        else:
            print("Error")
            break
    elif favorito in range(1, 6):
        counter = 0
        print('Usted ha elegido la opción número {}'.format(favorito))
        break
    elif favorito == 7:
        print('Hasta pronto')
        break
    else:
        counter += 1
