def Menu():
    print("MENU - RECURSIVIDAD")
    print("1 - FIBONACCI")
    print("2 - SUMATORIA DE N NUMEROS")
    print("3 - N-ESIMO FIBONACCI")
    print("4 - CANTIDAD DE LETRAS EN CADENA")
    print("5 - INVERTIR CADENA DE TEXTO")
    print("6 - CALCULAR POTENCIA DE UN NUMERO N")
    print("7. SALIR DEL MENU")
    print("OPCION A INGRESAR: ")


opcion = 0
while opcion != 7:
    opcion = input()
    match(opcion):
        case 1:
            print("FIBONACCI")
        case 2:
            print("SUMATORIA DE N NUMEROS")
        case 3:
            print("N-ESIMO FIBONACCI")
        case 4:
            print("CANTIDAD DE LETRAS EN CADENA")
        case 5:
            print("INVERTIR CADENA DE TEXTO")
        case 6:
            print("CALCULAR POTENCIA DE UN NUMERO N")
        case 7:
            print("SALIR DEL MENU")