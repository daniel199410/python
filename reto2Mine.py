from os import system, name
import sys

list_menu = ["Cambiar contraseña", "Ingresar coordenadas actuales", "Ubicar zona wifi más cercana",
             "Guardar archivo con ubicación cercana", "Actualizar registros de zonas wifi desde archivo",
             "Elegir opción de menú favorita", "Cerrar sesión"]
messages = ["Ingrese latitud", "Ingrese longitud"]
password = 23715
coordinates = []
m = 3


def welcome():
    print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
    user = 51732
    current_user = int(input("Nombre de usuario"))
    if current_user == user:
        password1 = int(input("Contraseña"))
        # captcha
        if password1 == password:
            number = 5 * 2 - 7 * 1
            captcha = int(input("Ingrese valor de la suma: 732+" + str(number)))
            if captcha == 732 + number:
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
    global coordinates
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


def update_coordinate(selected_option):
    for j in range(len(messages)):
        data = input(messages[j])
        if not data.strip():
            print("Error")
            sys.exit()
        else:
            data = float(data)
            if messages[0] == messages[j]:
                if not valid_lat(data):
                    print("Error coordenada")
                    sys.exit()
            else:
                if not valid_long(data):
                    print("Error coordenada")
                    sys.exit()
            coordinates[selected_option - 1][j] = data


def update_coordinates():
    selected_option = int(input("Presione 1,2 ó 3 para actualizar la respectiva coordenada. Presione 0 para regresar "
                                "al menú"))
    if selected_option in range(1, 4):
        update_coordinate(selected_option)
    else:
        print('Error actualización')
        sys.exit()
    print_list(list_menu)


def print_coordinates():
    gt = coordinates[0][0]
    long_sum = 0
    count = 0
    lat_sum = 0
    for i in range(m):
        print('coordenada [latitud,longitud] {} : {}'.format(i, coordinates[i]))
        if coordinates[i][0] > gt:
            gt = coordinates[i][0]
        count += 1
        long_sum += coordinates[i][0]
        lat_sum += coordinates[i][1]
    print('-Coordenada ubicada más al norte {}'.format(gt))
    print('-Coordenada promedio de todos los puntos. Latitud: {}'.format(long_sum / count))
    print('-Coordenada promedio de todos los puntos. Longitud {}'.format(lat_sum / count))


def main():
    coordinates_set = False
    welcome()
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
            if not coordinates_set:
                add_coordinates()
                coordinates_set = True
            else:
                print_coordinates()
                update_coordinates()
        elif favorito == 7:
            print('Hasta pronto')
            break
        else:
            print("Error")
            counter += 1


main()
