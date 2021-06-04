from os import system, name


def print_list(_list_):
    x = 0
    txt = ''
    while x < len(_list_):
        txt = '{} {}'.format(txt, '{}. {}'.format(x + 1, _list_[x]))
        if x < len(_list_) - 1:
            txt = txt + ","
        else:
            txt = txt + "."
        x += 1
    print(txt)


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


list_menu = ["Cambiar contraseña", "Ingresar coordenadas actuales", "Ubicar zona wifi más cercana",
             "Guardar archivo con ubicación cercana", "Actualizar registros de zonas wifi desde archivo",
             "Elegir opción de menú favorita", "Cerrar sesión"]
print_list(list_menu)
counter = 0
while counter < 4:
    print("Elija una opción")
    favorito = int(input(""))
    if favorito == 6:
        counter = 0
        print("Seleccione opción favorita")
        favorita = int(input(""))
        if favorita in range(1, 6):
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
        print("Error")
        counter += 1
