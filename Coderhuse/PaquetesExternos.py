
# from collections import *
# namedtuple #asignar nombres especificos a una tupla (ayuda a que el codigo tenga nombres mas claros)

# pez = namedtuple("pez", ["nombre", "especie", "peso"])
# pez1 = pez ("pecesin", "payaso", "1")

# print(pez)

# from collections import Counter

# # lista = [1,2,3,4,4,4,5,6]

# # print(Counter(lista))

# estudiantes =  "mateo milagro nicolas bautista"

# print(Counter(estudiantes))
# print(Counter(estudiantes.split()))

# from datetime import *

# dt = datetime.now()

# dt_prueba = datetime(2000, 1, 1)

# dt_prueba= dt_prueba.replace(2020)
# print(dt.year)
# print(dt.month)
# print(dt.day)
# print(dt_prueba.day)

# %A: DIA DE LA SEMANA
# %d: dia del mes
# %B: nombre del mes
# %Y: año
# %I: hora
# %M: minutos

# print(dt.strftime("%A %d %B %Y %I %M"))

# t = timedelta(days=14, hours=4, seconds=1000)

# dt_dentro_de_dos_semanas = dt + t
# print(dt)
# print(dt_dentro_de_dos_semanas)

# import math
# #raisz cuadrada
# x = math.sqrt(64.74646)

# print(f"la raiz cuadrada de el numero es {x}")

# #redondeo al entero mas cercano

# x = math. ceil(1.4) #redondea para arriba
# y = math. floor(1.4) #redondea hacia el menor

# print(f"Primer redondeo {x}") #ceil
# print(f"Segundo redondeo {y}") #floor

import random

print(random.randrange(0, 20, step= 3))

string = "esta es una prueba de random"
lista = [1,2,"mateo", 0]

print("este es un random tomado de este string:", random.choice(string))
print("este es un random tomado de esta lista:", random.choice(lista))