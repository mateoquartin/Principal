cadena = "mateo quartin"
cadena2 = ["mateo", "quartin"]
cadena_strip = "    mateo     "
#todas estas funciones estan tirando una copia con la funcion aplicada (no modifica el string, un string no se modifica)
print(cadena.lower())#minusculas
print(cadena.upper())#mayusculas
print(cadena.capitalize())#sirve para devolver la cadena con la primera en mayusculas
print(cadena.title())#devuelve cada uno de las palabras con la primera en mayusculas
print(cadena.count("o")) #me devuelve las cantidad de veces que esta en el string
print(cadena.find("o")) #devuelve el indice del primer elemento encontrado / si no encuentra nada es -1
print(cadena.rfind("a"))#devuelve la ultima o la primera empezando desde el ultimo 
print(cadena.split())#separa la lista y vos le indicas el parametro para separar
print("".join(cadena2)) # une una lista de elementos separados 
print(",".join(cadena2))
print(cadena_strip.strip())#elimina de la derecha y la izquierda el carcater indicado
print(cadena.replace("mateo", "lautaro")) =


