filas = int(input("ingresar cantidad de filas: "))
columnas = int(input("ingresar cantidad de columnas: "))
matriz = []
for i in range(filas):
    matriz.append([None]*columnas)
for i in range (filas):
    for j in range (columnas):
        valor = input("ingresar valor")
        matriz [i][j]=valor
# Usar un ciclo for para recorrer cada fila de la matriz
for fila in matriz:
    # Usar otro ciclo for para recorrer cada elemento de la fila
    for elemento in fila:
        # Imprimir el elemento
        print(elemento, end=' ')
    # Imprimir un salto de línea al final de cada fila
    print()