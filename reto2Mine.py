from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def print_list(_list_):
    i = 0
    while i < len(_list_):
        print('{}. {}'.format(i + 1, _list_[i]))
        i += 1


list_menu = ["Cambiar contraseña", "Ingresar coordenadas actuales", "Ubicar zona wifi más cercana",
             "Guardar archivo con ubicación cercana", "Actualizar registros de zonas wifi desde archivo",
             "Elegir opción de menú favorita", "Cerrar sesión"]
counter = 0
print_list(list_menu)
while counter < 3:
    print("Elija una opción")
    favorito = int(input(""))
    if favorito == 6:
        print("Seleccione opción favorita")
        favorita = int(input(""))
        if favorita in range(1, 6):
            counter = 0
            adivinanza1 = int(input(
                "Para confirmar por favor responda:Me separaron de mi hermano siamés,antes era un ocho y ahora "
                "soy un: "))
            if adivinanza1 == 3:
                adivinanza2 = int(input(
                    "Para confirmar por favor responda:Soy más de uno sin llegar al tres, y llego a cuatro cuando dos "
                    "me des: "))
                if adivinanza2 == 2:
                    eliminado = list_menu.pop(favorita - 1)
                    list_menu.insert(0, eliminado)
                    clear()
                else:
                    print("Error")
            else:
                print("Error")
            print_list(list_menu)
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
