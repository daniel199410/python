from os import system, name
import sys

password = 23715
coordenadas = []
messages = ["Ingrese latitud", "Ingrese longitud"]


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
        else:
            print("Error")

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


list_menu = ["Cambiar contraseña", "Ingresar coordenadas actuales", "Ubicar zona wifi más cercana",
             "Guardar archivo con ubicación cercana", "Actualizar registros de zonas wifi desde archivo",
             "Elegir opción de menú favorita", "Cerrar sesión"]
#welcome()
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
    elif favorito in range(4, 6):
        counter = 0
        print('Usted ha elegido la opción {}'.format(favorito))
        break
    elif favorito == 1:
        confirmation = int(input("Confirmar la contraseña actual "))
        if confirmation == password:
            newPassword = int(input("Nueva contraseña del usuario "))
            print_list(list_menu)

        else:
            print("Error")
            break
    elif favorito == 2:
        if len(coordenadas) == 0:
            m = 3
            # llenar matriz  #Sup 6.306 Inf: 5.888 or:-72.321 occ:-72.552

            for i in range(m):
                a = []
                for j in messages:
                    datos1 = input(j)
                    if not datos1.strip():
                        print("Error")
                        sys.exit()
                    datos1 = float(datos1)
                    if j == messages[0]:
                        if datos1 > 6.306 or datos1 < 5.888:
                            print("Error coordenada")
                            sys.exit()

                    else:
                        if datos1 > -72.321 or datos1 < -72.552:
                            print("Error coordenada")
                            sys.exit()

                    a.append(datos1)
                coordenadas.append(a)
            # print(coordenadas)
            print_list(list_menu)
        else:
            contador2 = 0
            gt = coordenadas[0][0]
            mayor = 1
            mt = coordenadas[0][1]
            menor = 1
            for i in coordenadas:
                if coordenadas[contador2][0] > gt:
                    gt = coordenadas[contador2][0]
                    mayor = contador2 + 1

                if coordenadas[contador2][1] < mt:
                    mt = coordenadas[contador2][1]
                    menor = contador2 + 1
                contador2 += 1
                print("coordenada [latitud, longitud] {}:  {}".format(contador2, i))
            print("La coordenada {} es la que está más al norte".format(mayor))
            print("La coordenada {} es la que está más al occidente".format(menor))
            seleccion = int(
                input("Presione 1,2 ó 3 para actualizar la respectiva coordenada. Presione 0 para regresar al menú"))
            if seleccion == 0:
                print_list(list_menu)
            elif seleccion in range(1, 4):
                for j in range(len(messages)):

                    datos1 = input(messages[j])
                    if not datos1.strip():
                        print("Error")
                        sys.exit()
                    datos1 = float(datos1)
                    if messages[j] == messages[0]:
                        if datos1 > 6.306 or datos1 < 5.888:
                            print("Error coordenada")
                            sys.exit()

                    else:
                        if datos1 > -72.321 or datos1 < -72.552:
                            print("Error coordenada")
                            sys.exit()
                    coordenadas[seleccion - 1][j] = datos1
            else:
                print("Error actualización")
                sys.exit()
    elif favorito == 3:
        matriz = [[6.211, -72.482, 2], [6.212, -72.470, 25], [6.105, -72.342, 25], [6.210, -72.442, 50], [6.105, -72.342, 25], [6.210, -72.442, 50]]
        for row in coordenadas:
            for column in row:
                print(column)


    elif favorito == 7:
        print('Hasta pronto')
        break
    else:
        print("Error")
        counter += 1
