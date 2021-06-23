import os.path
from os import system, name
import sys
import csv
import math

FILE_NAME = 'Acceso_universal'
list_menu = ["Cambiar contraseña", "Ingresar coordenadas actuales", "Ubicar zona wifi más cercana",
             "Guardar archivo con ubicación cercana", "Actualizar registros de zonas wifi desde archivo",
             "Elegir opción de menú favorita", "Cerrar sesión"]
transport_time = ["Tiempo en bus", "Tiempo en auto"]
preferred_coordinates = [
    {"long": 6.211, "lat": -72.482, "user_average": 2},
    {"long": 6.212, "lat": -72.470, "user_average": 25},
    {"long": 6.105, "lat": -72.242, "user_average": 25},
    {"long": 6.210, "lat": -72.442, "user_average": 50},
]
messages = ["Ingrese latitud", "Ingrese longitud"]
password = 23715
coordinates = []
closest_zones = []
m = 3
current_position = -1
zone_option = 0


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
        guess1 = int(input(
            "Para confirmar por favor responda:Me separaron de mi hermano siamés,antes era un ocho y ahora "
            "soy un: "))
        if guess1 == 3:
            guess2 = int(input(
                "Para confirmar por favor responda:Soy más de uno sin llegar al tres, y llego a cuatro cuando dos "
                "me des: "))
            if guess2 == 2:
                deleted = list_menu.pop(favorite - 1)
                list_menu.insert(0, deleted)
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


def print_only_coordinates():
    greatest_latitude_value = coordinates[0][0]
    greatest_longitude_value = coordinates[0][1]
    count = 0
    for i in range(m):
        print('coordenada [latitud,longitud] {} : {}'.format(i + 1, coordinates[i]))
        if coordinates[i][0] > greatest_latitude_value:
            greatest_latitude_value = coordinates[i][0]
        if coordinates[i][1] > greatest_longitude_value:
            greatest_latitude_value = coordinates[i][1]
        count += 1


def print_coordinates():
    greatest_latitude_value = coordinates[0][0]
    greatest_longitude_value = coordinates[0][1]
    greatest_latitude_coordinate = 1
    greatest_longitude_coordinate = 1
    count = 0
    for i in range(m):
        print('coordenada [latitud,longitud] {} : {}'.format(i + 1, coordinates[i]))
        if coordinates[i][0] > greatest_latitude_value:
            greatest_latitude_value = coordinates[i][0]
            greatest_latitude_coordinate = count + 1
        if coordinates[i][1] > greatest_longitude_value:
            greatest_latitude_value = coordinates[i][1]
            greatest_longitude_coordinate = count + 1
        count += 1
    print('La coordenada {} es la que está más al norte'.format(greatest_latitude_coordinate))
    print('La coordenada {} es la que está más al occidente'.format(greatest_longitude_coordinate))


def calculate_distance(param, coordinate):
    _R_ = 6372.795477598
    lat_delta = coordinate["lat"] - param[0]
    lon_delta = coordinate["long"] - param[1]
    return 2 * _R_ * math.asin(
        math.sqrt(
            math.pow(math.sin(lat_delta / 2), 2)
            + math.cos(param[0])
            * math.cos(coordinate["lat"])
            * math.pow(math.sin(lon_delta / 2), 2)
        )
    )


def locate_two_closest_wifi_zone(param):
    closest_coordinates = []
    return_coordinates = []
    for coordinate in preferred_coordinates:
        closest_coordinates.append({"coordinates": coordinate, "distance": calculate_distance(param, coordinate)})
    for i in range(len(closest_coordinates)):
        for j in range(len(closest_coordinates) - i):
            if closest_coordinates[j]["distance"] > closest_coordinates[i]["distance"]:
                temp = closest_coordinates[j]
                closest_coordinates[j] = closest_coordinates[i]
                closest_coordinates[i] = temp
    for i in range(1, 3):
        return_coordinates.append(closest_coordinates[i])
    for i in range(len(return_coordinates)):
        for j in range(len(return_coordinates)):
            if return_coordinates[j]["coordinates"]["user_average"] > \
                    return_coordinates[i]["coordinates"]["user_average"]:
                temp = return_coordinates[j]
                return_coordinates[j] = return_coordinates[i]
                return_coordinates[i] = temp
    return return_coordinates


def calculate_direction(user_coordinates, preferred_coordinate):
    is_eastern = 'oriente'
    is_north = 'norte'
    if user_coordinates[0] < preferred_coordinate["coordinates"]["long"]:
        is_eastern = 'occidente'
    if user_coordinates[1] < preferred_coordinate["coordinates"]["lat"]:
        is_eastern = 'sur'
    return {"long": is_eastern, "lat": is_north}


def calculate_transport_time(wifi_distance):
    average_bus_speed = 20.83
    if zone_option == 1:
        average_bus_speed = 16.67
    return wifi_distance / average_bus_speed


def locate_closest_wifi_zone():
    global closest_zones
    global current_position
    global zone_option
    if len(coordinates) == 0:
        print('Error sin registro de coordenadas')
        sys.exit()
    print_only_coordinates()
    current_position = int(
        input("Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de "
              "conexión"))
    if current_position not in range(len(coordinates) + 1):
        print('Error ubicación')
        sys.exit()
    closest_zones = locate_two_closest_wifi_zone(coordinates[current_position - 1])
    print('Zonas wifi cercanas con menos usuarios')
    for i in range(2):
        print('La zona wifi {}: ubicada en [{}, {}] a {} metros , tiene un promedio de {} usuarios'.format(
            i + 1,
            closest_zones[i]["coordinates"]["long"],
            closest_zones[i]["coordinates"]["lat"],
            int(closest_zones[i]["distance"]),
            closest_zones[i]["coordinates"]["user_average"]
        ))
    zone_option = int(input('Elija 1 o 2 para recibir indicaciones de llegada'))
    if zone_option not in range(1, 3):
        print('Error zona wifi')
        sys.exit()
    directions = calculate_direction(coordinates[current_position - 1], closest_zones[zone_option - 1])
    print('Para llegar a la zona wifi dirigirse primero al {} y luego hacia el {}'.format(directions["long"],
                                                                                          directions["lat"]))
    print('Tiempo promedio: {} m/s'.format(calculate_transport_time(closest_zones[0]["distance"])))
    _exit_ = 1
    while _exit_ != 0:
        _exit_ = int(input('Presione 0 para salir'))
    print_list(list_menu)


def export_to_file():
    global current_position
    if len(coordinates) == 0 or current_position < 0:
        print('Error de alistamiento')
        sys.exit()
    wifi_zone_coordinates = closest_zones[zone_option - 1]["coordinates"]
    distance = int(closest_zones[zone_option - 1]["distance"])
    average_time = calculate_transport_time(closest_zones[zone_option - 1]["distance"])
    information = {
        'actual': coordinates[current_position - 1],
        'zonawifi{}'.format(zone_option): [wifi_zone_coordinates["long"], wifi_zone_coordinates["lat"],
                                           wifi_zone_coordinates["user_average"]],
        'recorrido': [distance, 'Bus', average_time]
    }
    print(information)
    option = int(input('Presione 1 para confirmar, 0 para regresar al menú principal'))
    if option == 1:
        print('Exportando archivo')
        file = open('dictionary.txt', 'w')
        file.write(str(information))
        file.close()
        sys.exit()
    if option == 0:
        print_list(list_menu)
    else:
        sys.exit()


def import_from_file():
    global preferred_coordinates
    if os.path.isfile(FILE_NAME + ".csv"):
        file = open(FILE_NAME + ".csv")
    else:
        file = open(FILE_NAME + ".txt")
    reader = csv.reader(file)
    preferred_coordinates = []
    counter = 1
    for row in reader:
        if not row[0].isnumeric():
            continue
        long = float(row[10].replace(',', '.'))
        lat = float(row[11].replace(',', '.'))
        users = 0
        if row[16] != '':
            users = int(row[16])
        preferred_coordinates.append({"long": long, "lat": lat, "user_average": users})
        counter += 1
        if counter == 5:
            break
    while True:
        option = int(input("Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú "
                           "principal"))
        if option == 0:
            break
    print_list(list_menu)


def main():
    coordinates_set = False
    welcome()
    print_list(list_menu)
    counter = 0
    while counter < 4:
        print("Elija una opción")
        favorite = int(input(""))
        if favorite == 1:
            change_password()
        elif favorite == 2:
            if not coordinates_set:
                add_coordinates()
                coordinates_set = True
            else:
                print_coordinates()
                update_coordinates()
        elif favorite == 3:
            locate_closest_wifi_zone()
        elif favorite == 4:
            export_to_file()
        elif favorite == 5:
            import_from_file()
        elif favorite == 6:
            set_favorite()
        elif favorite == 7:
            print('Hasta pronto')
            break
        else:
            print("Error")
            counter += 1


main()
