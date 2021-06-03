import os

menu_lista = ["1. Cambiar contraseña", "2. Ingresar coordenadas actuales", "3. Ubicar zona wifi más cercana",
              "4. Guardar archivo con ubicación cercana", "5. Actualizar registros de zonas wifi desde archivo",
              "6. Elegir opción de menú favorita", "7. Cerrar sesión"]
print(menu_lista)
while menu_lista:
    print("Elija una opción")
    favorito = int(input(""))
    if favorito == 6:
        print("Seleccione opción favorita")
        favorita = int(input(""))
        if favorita >= 1 <= 5:
            adivinanza1 = int(input(
                "Para confirmar por favor responda:Me separaron de mi hermano siamés,antes era un ocho y ahora soy un: "))
            if adivinanza1 == 3:
                adivinanza2 = int(input(
                    "Para confirmar por favor responda:Soy más de uno sin llegar al tres, y llego a cuatro cuando dos me des: "))
                if adivinanza2 == 2:
                    eliminado = menu_lista.pop(favorita)
                    insertado = menu_lista.insert(0, eliminado)
                    os.system("cls")
                else:
                    print("Error")
            else:
                print("Error")
            print(menu_lista)
        else:
            print("Error")
    elif favorito in range(1, 6):
        print('Usted ha elegido la opción número {}'.format(favorito))
        break
    else:
        print("Hasta pronto")
        break
