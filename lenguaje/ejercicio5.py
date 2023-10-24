def calcular_potecncia(n,k):
    potencia = n**k
    return potencia

def cantidad_digitos(numero):
    numero_cadena = str(numero)
    print(len(numero_cadena))

def es_capicua(numero):
    cadena_numero = str(numero)
    numero_invertido = cadena_numero[::-1]
    return numero_invertido == cadena_numero

while True:
    print("---Bienvenido al menu---")
    print("1-Calcular potencia de un numero: ")
    print("2-Calcular digitos")
    print("3-Calcular capicua")
    print("0-salir")
    opcion = int(input("Ingresar la opcion a realizar: "))
    if opcion == 1:
        n = int(input("Ingresar numero: "))
        k = int(input("ingresar potrncia: "))
        calcular_potecncia(n, k)
    elif opcion == 2:
        n = int(input("Ingresar numero: "))
        cantidad_digitos(n)
    elif opcion == 3:
        n = int(input("Ingresar numero: "))
        es_capicua(n)
        if es_capicua(n):
            print(f"el numero {n} es capicua")
        else:
            print(f"el numero {n} no es capicua")
    elif opcion == 0:
        break
    




