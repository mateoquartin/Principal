# Función para cargar un nuevo dominio en una matriz
def cargar_nuevo_dominio(matriz):
    patente = input("Ingrese la patente del vehículo: ")
    dni = input("Ingrese el DNI del propietario: ")
    apellido_nombre = input("Ingrese el Apellido y Nombre del propietario: ")
    modelo = input("Ingrese el modelo del vehículo (año): ")
    provincia = input("Ingrese la provincia de radicación: ")

    # Validación de que la patente no exista previamente
    for dominio in matriz:
        if dominio[0] == patente:
            print("Error: La patente ingresada ya existe en la lista.")
            return

    # Validación de que el DNI y modelo sean datos numéricos
    if not dni.isdigit() or not modelo.isdigit():
        print("Error: El DNI y el modelo deben ser datos numéricos.")
        return

    nuevo_dominio = [patente, dni, apellido_nombre, modelo, provincia]
    matriz.append(nuevo_dominio)
    print("Nuevo dominio cargado correctamente.\n")


# Función para buscar dominio por cualquier dato
def buscar_dominio_por_dato(matriz):
    criterio_busqueda = input("Ingrese el dato para buscar el dominio: ")
    resultados_encontrados = []

    for dominio in matriz:
        if criterio_busqueda.lower() in [dato.lower() for dato in dominio]:
            resultados_encontrados.append(dominio)

    if resultados_encontrados:
        print("Resultados encontrados:")
        for resultado in resultados_encontrados:
            print("Patente:", resultado[0])
            print("DNI:", resultado[1])
            print("Apellido y Nombre:", resultado[2])
            print("Modelo:", resultado[3])
            print("Provincia:", resultado[4])
            print("-----------------------")
    else:
        print("No se encontraron dominios que coincidan con el criterio de búsqueda.\n")


# Función para eliminar un dominio de la lista
def eliminar_dominio_por_patente(matriz):
    patente_buscar = input("Ingrese la patente del dominio a eliminar: ")

    dominio_encontrado = None
    for dominio in matriz:
        if dominio[0] == patente_buscar:
            dominio_encontrado = dominio
            break

    if dominio_encontrado:
        matriz.remove(dominio_encontrado)
        print("Dominio con patente", patente_buscar, "eliminado correctamente.")
    else:
        print("Error: No se encontró ningún dominio con la patente", patente_buscar)


# Función para modificar un dominio en la lista
def modificar_dominio_por_patente(matriz):
    patente_buscar = input("Ingrese la patente del dominio a modificar: ")

    dominio_encontrado = None
    for dominio in matriz:
        if dominio[0] == patente_buscar:
            dominio_encontrado = dominio
            break

    if dominio_encontrado:
        dni = input("Ingrese el nuevo DNI del propietario: ")
        modelo = input("Ingrese el nuevo modelo del vehículo (año): ")

        # Validación de que el DNI y modelo sean datos numéricos
        if not dni.isdigit() or not modelo.isdigit():
            print("Error: El DNI y el modelo deben ser datos numéricos.")
            return

        dominio_encontrado[1] = dni
        dominio_encontrado[3] = modelo
        print("Dominio con patente", patente_buscar, "modificado correctamente.")
    else:
        print("Error: No se encontró ningún dominio con la patente", patente_buscar)


# Función principal para el menú
def main():
    matriz_dominios = []  # Inicializamos la matriz vacía

    while True:
        print("-------- Menú --------")
        print("a) Cargar nuevo dominio")
        print("b) Buscar dominio por cualquier dato")
        print("c) Eliminar un dominio de la lista")
        print("d) Modificar un dominio de la lista")
        print("x) Salir")

        opcion = input("Seleccione una opción: ")

        if opcion.lower() == 'a':
            cargar_nuevo_dominio(matriz_dominios)
        elif opcion.lower() == 'b':
            buscar_dominio_por_dato(matriz_dominios)
        elif opcion.lower() == 'c':
            eliminar_dominio_por_patente(matriz_dominios)
        elif opcion.lower() == 'd':
            modificar_dominio_por_patente(matriz_dominios)
        elif opcion.lower() == 'x':
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.\n")


if __name__ == "__main__":
    main()
    