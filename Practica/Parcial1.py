def cargar_matriz(filas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(2):
            elemento = input(f"Ingresar valor para la fila {i+1}, columna {j+1}: ")
            fila.append(elemento)
        matriz.append(fila)
    return matriz

def crear_matriz_b(matriz_a):
    matriz_b = []
    for i, fila in enumerate(matriz_a):
        fila_b = [i + 1, max(len(word) for word in fila)]
        matriz_b.append(fila_b)
    return matriz_b

def mostrar_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end="\t")
        print()
def mostrar_indices_pares(matriz_b):
    indices_pares = []
    for i, fila in enumerate(matriz_b):
        for j, valor in enumerate(fila):
            if valor % 2 == 0:
                indices_pares.append((i + 1, j + 1))  # Sumamos 1 para contar desde 1, no desde 0
    if indices_pares:
        print("Índices de filas y columnas con números pares:")
        for fila, columna in indices_pares:
            print(f"Fila: {fila}, Columna: {columna}")
    else:
        print("No se encontraron números pares en la matriz B.")

# Menú
while True:
    print("------- Menú -------")
    print("a) Cargar la matriz A")
    print("b) Crear matriz B")
    print("c) Mostrar matrices")
    print("d) Mostrar índices de filas y columnas con números pares en matriz B")
    print("e) Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "a":
        filas = int(input("Ingrese el número de filas de la matriz A: "))
        matriz_a = cargar_matriz(filas)
    elif opcion == "b":
        if "matriz_a" in locals():
            matriz_b = crear_matriz_b(matriz_a)
        else:
            print("Por favor, primero cargue la matriz A.")
    elif opcion == "c":
        if "matriz_a" in locals() and "matriz_b" in locals():
            print("Matriz A:")
            mostrar_matriz(matriz_a)
            print("Matriz B:")
            mostrar_matriz(matriz_b)
        else:
            print("Por favor, primero cargue la matriz A y luego cree la matriz B.")
    elif opcion == "d":
        if "matriz_b" in locals():
            mostrar_indices_pares(matriz_b)
        else:
            print("Por favor, primero cree la matriz B.")
    elif opcion == "e":
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")