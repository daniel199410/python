from os import system, name
import sys

password = 23715


def welcome():
    print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
    usuario = 51732
    # usuario y contraseña
    usuario1 = int(input("Nombre de usuario"))
    if usuario1 == usuario:
        password1 = int(input("Contraseña"))
        # captcha
        if password1 == password:
            numero = 5 * 2 - 7 * 1
            captcha = int(input("Ingrese valor de la suma: 732+" + str(numero)))
            if captcha == 732 + numero:
                print("Sesión iniciada")
            else:
                print("Error")
                sys.exit()
        else:
            print("Error")
            sys.exit()
    else:
        print("Error")
        sys.exit()


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


def set_favorite():
    print("Seleccione opción favorita")
    favorite = int(input(""))
    if favorite in range(1, 6):
        adivinanza1 = int(input(
            "Para confirmar por favor responda:Me separaron de mi hermano siamés,antes era un ocho y ahora "
            "soy un: "))
        if adivinanza1 == 3:
            adivinanza2 = int(input(
                "Para confirmar por favor responda:Soy más de uno sin llegar al tres, y llego a cuatro cuando dos "
                "me des: "))
            if adivinanza2 == 2:
                eliminado = list_menu.pop(favorite - 1)
                list_menu.insert(0, eliminado)
                clear()
            else:
                print("Error")
        else:
            print("Error")
        print_list(list_menu)
    else:
        print("Error")
        sys.exit()


def valid_long(data):
    return -72.321 >= data >= -72.552


def valid_lat(data):
    return 6.306 >= data >= 5.888


def add_coordinates():
    coordinates = []
    m = 3
    messages = ["Ingrese latitud", "Ingrese longitud"]
    for i in range(m):
        a = []
        for j in messages:
            data = input(j)
            if not data.strip():
                print("Error")
                sys.exit()
            else:
                data = float(data)
                if messages[0] == j:
                    if not valid_lat(data):
                        print("Error coordenada")
                        sys.exit()
                else:
                    if not valid_long(data):
                        print("Error coordenada")
                        sys.exit()
                a.append(data)
        coordinates.append(a)
    print_list(list_menu)


def change_password():
    confirmation = int(input("Confirme contraseña actual: "))
    global password
    if confirmation == password:
        password = int(input("Nueva contraseña de usuario"))
        print_list(list_menu)
    else:
        print("Error")
        sys.exit()


list_menu = ["Cambiar contraseña", "Ingresar coordenadas actuales", "Ubicar zona wifi más cercana",
             "Guardar archivo con ubicación cercana", "Actualizar registros de zonas wifi desde archivo",
             "Elegir opción de menú favorita", "Cerrar sesión"]


def main():
    # welcome()
    print_list(list_menu)
    counter = 0
    while counter < 4:
        print("Elija una opción")
        favorito = int(input(""))
        if favorito == 6:
            set_favorite()
        elif favorito in range(3, 6):
            print('Usted ha elegido la opción {}'.format(favorito))
            break
        elif favorito == 1:
            change_password()
        elif favorito == 2:
            add_coordinates()
        elif favorito == 7:
            print('Hasta pronto')
            break
        else:
            print("Error")
            counter += 1


main()
