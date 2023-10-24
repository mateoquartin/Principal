def cargar_matriz (filas, columnas):
    matriz = []
    for i in range (filas):
        fila = []
        for j in range (columnas):
            elemento = input(f"ingresar valor {i+1}{j+1}: ")
            fila.append(elemento)
        matriz.append(fila)
    return(matriz)

def mostrar_matriz (matriz):
    for fila in matriz:
        for elemento in fila:
            print (elemento, end="\t")
        print()

def eliminar_elementos_repetidos(matriz):
    elementos_unicos = set()
    matriz_sin_repetidos = []
    for fila in matriz:
        fila_sin_repetidos = []
        for elemento in fila:
            if elemento not in elementos_unicos:
                elementos_unicos.add(elemento)
                fila_sin_repetidos.append(elemento)
        matriz_sin_repetidos.append(fila_sin_repetidos)

    return matriz_sin_repetidos

filas = int(input("ingresar cantidad de filas: "))
columnas = int(input("ingresar cantidad de columnas: "))
matriz = cargar_matriz(filas, columnas)
print ("matriz cargada: ")
mostrar_matriz(matriz)

matriz_ordenada = sorted(matriz, key=lambda fila: fila[0])
print ("matriz ordenada")
mostrar_matriz(matriz_ordenada)

matriz_sin_repetidos = eliminar_elementos_repetidos(matriz)
print ("matriz sin repetidos")
mostrar_matriz(matriz_sin_repetidos)

