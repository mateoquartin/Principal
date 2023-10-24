# parcial deudas municipalidad



def leer_datos_archivo(nombre_archivo):
    deudas = []
    with open(nombre_archivo, 'r') as file:
        for line in file:
            patente = line[0:7]
            periodo = line[7:11]
            deuda = float(line[11:16])
            deudas.append({
                'patente': patente,
                'periodo': periodo,
                'deuda': deuda
            })
    return deudas

def mostrar_patentes_por_deuda(deudas, valor):
    patentes_deuda_superior = [deuda['patente'] for deuda in deudas if deuda['deuda'] > valor]
    return patentes_deuda_superior

def generar_matriz_ordenada_por_deuda(deudas):
    matriz_ordenada = sorted(deudas, key=lambda x: x['deuda'], reverse=True)
    return matriz_ordenada

def generar_archivo_exportar(deudas, nombre_archivo_salida):
    with open(nombre_archivo_salida, 'w') as file:
        for deuda in deudas:
            linea = f"{deuda['patente']},{deuda['periodo']},{deuda['deuda']:.2f}\n"
            file.write(linea)

# Programa principal
def menu():
    archivo_deudas = "deudas.txt"
    deudas = leer_datos_archivo(archivo_deudas)

    while True:
        print("\nMenú:")
        print("a) Mostrar patentes cuya deuda supera un valor ingresado")
        print("b) Generar matriz ordenada por deuda (mayor a menor)")
        print("c) Generar archivo exportar.txt con los datos separados por comas")
        print("x) Salir")

        opcion = input("Ingrese la opción deseada: ")

        if opcion.lower() == 'a':
            valor_ingresado = float(input("Ingrese el valor para comparar con las deudas: "))
            patentes_deuda_superior = mostrar_patentes_por_deuda(deudas, valor_ingresado)
            print("Patentes con deuda superior al valor ingresado:")
            print(patentes_deuda_superior)

        elif opcion.lower() == 'b':
            matriz_ordenada_por_deuda = generar_matriz_ordenada_por_deuda(deudas)
            print("Matriz ordenada por deuda (mayor a menor):")
            for deuda in matriz_ordenada_por_deuda:
                print(deuda)

        elif opcion.lower() == 'c':
            archivo_exportar = "exportar.txt"
            generar_archivo_exportar(deudas, archivo_exportar)
            print(f"Archivo {archivo_exportar} generado exitosamente.")

        elif opcion.lower() == 'x':
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Por favor, ingrese una opción válida (a, b, c o x).")

# Llamamos a la función menu para ejecutar el programa
menu()