filas = int(input("ingresar cantidad de filas: "))
columnas = int(input("ingresar cantidad de columnas: "))
matriz = []
for i in range (filas):
    fila = []
    for j in range (columnas):
        valor = input(f"ingresar valor {i+1}{j+1}:")
        fila.append(valor)
    matriz.append (fila)

for fila in matriz:
    for elemento in fila:
        print(elemento, end= " ")
    print()