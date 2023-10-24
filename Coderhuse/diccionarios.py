colores = {"amarillo": "yellow", "azul": "blue"}
print(len(colores))
colores.update({"rojo": "red"})
print(colores["rojo"])
del colores["amarillo"] # borramos el elemento del dicc
print(colores)
print("rojo" in colores)
colores.clear() #vaciamos el dicc
print(colores)
print("red"in colores )

my_set = {2,2,3,4,2,5}
print(my_set)