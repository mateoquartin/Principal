# Función para leer el archivo de texto y obtener los datos en una lista de diccionarios
def leer_datos_archivo(nombre_archivo):
    empleados = []
    with open(nombre_archivo, 'r') as file:
        for line in file:
            dni = int(line[0:8])
            legajo = int(line[8:12])
            apellido_nombre = line[12:25].strip()
            sueldo = float(line[25:32])
            empleados.append({
                'dni': dni,
                'legajo': legajo,
                'apellido_nombre': apellido_nombre,
                'sueldo': sueldo
            })
    return empleados

# a) Mostrar la cantidad de empleados
def cantidad_empleados(empleados):
    return len(empleados)

# b) Mostrar el monto total de sueldos a depositar
def monto_total_sueldos(empleados):
    total_sueldos = sum(empleado['sueldo'] for empleado in empleados)
    return total_sueldos

# Función auxiliar para ordenar los datos por una clave específica
def ordenar_por_clave(empleados, clave):
    return sorted(empleados, key=lambda x: x[clave])

# c) Ordenar y mostrar los datos en una matriz, por sueldos.
def ordenar_por_sueldos(empleados):
    empleados_ordenados = ordenar_por_clave(empleados, 'sueldo')
    return empleados_ordenados

# d) Ordenar y mostrar los datos en una matriz, por legajo.
def ordenar_por_legajo(empleados):
    empleados_ordenados = ordenar_por_clave(empleados, 'legajo')
    return empleados_ordenados

# e) Generar un nuevo archivo de texto con valores numéricos completados con ceros a la izquierda.
def generar_archivo_con_ceros(empleados, nombre_archivo_salida):
    with open(nombre_archivo_salida, 'w') as file:
        for empleado in empleados:
            dni = str(empleado['dni']).zfill(8)
            legajo = str(empleado['legajo']).zfill(4)
            apellido_nombre = empleado['apellido_nombre']
            sueldo = str(empleado['sueldo']).zfill(7)
            linea = f"{dni} : {legajo} : {apellido_nombre:<13} : {sueldo}\n"
            file.write(linea)

# Programa principal
if __name__ == "__main__":
    archivo_entrada = "c:/sueabr11.txt"
    archivo_salida = "c:/sueabr11ban.txt"

    empleados = leer_datos_archivo(archivo_entrada)

    # a) Mostrar la cantidad de empleados
    print("Cantidad de empleados:", cantidad_empleados(empleados))

    # b) Mostrar el monto total de sueldos a depositar
    print("Monto total de sueldos a depositar:", monto_total_sueldos(empleados))

    # c) Ordenar y mostrar los datos por sueldos
    empleados_ordenados_por_sueldo = ordenar_por_sueldos(empleados)
    print("\nEmpleados ordenados por sueldo:")
    for empleado in empleados_ordenados_por_sueldo:
        print(empleado)

    # d) Ordenar y mostrar los datos por legajo
    empleados_ordenados_por_legajo = ordenar_por_legajo(empleados)
    print("\nEmpleados ordenados por legajo:")
    for empleado in empleados_ordenados_por_legajo:
        print(empleado)

    # e) Generar el nuevo archivo de texto con valores completados con ceros a la izquierda
    generar_archivo_con_ceros(empleados, archivo_salida)
    print("\nNuevo archivo generado:", archivo_salida)
