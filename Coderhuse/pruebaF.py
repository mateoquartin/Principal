import numpy as np

# Cargamos los datos desde el archivo
archivo_datos = "C:\FACULTAD\Todo python\Coderhuse\\total-usuarios-por-dia(1).txt"
try:
    data = np.genfromtxt(archivo_datos, delimiter=",", dtype=str, skip_header=1)
except FileNotFoundError:
    print(f"Error: No se pudo encontrar el archivo '{archivo_datos}'.")
except Exception as e:
    print(f"Error inesperado: {e}")


# Filtramos los datos para quedarnos solo con el año 2020
data_2020 = data[data[:, 0] == '2020']

# Convertimos la columna de meses a números enteros
meses_2020 = data_2020[:, 1].astype(int)

# Encontramos el mes con mayor uso en 2020
mes_con_mas_uso = np.argmax(meses_2020) + 1  # Sumamos 1 para obtener el mes en lugar del índice

# Imprimimos el resultado
print(f"El mes con mayor uso de lancha en 2020 es el mes {mes_con_mas_uso}")
