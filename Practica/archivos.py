

def carga_vector (vec, tam):
    for i in range (tam):
        vec[i] = input("ingresar palabra: ")

def salta_linea (vec, tam):
    for i in range (tam):
        vec[i] = vec[i] + "\n"

tam = int(input("ingresar tamaño de la lista: "))
vec = [None]*tam
carga_vector(vec, tam)
salta_linea(vec, tam)
archivo = open("C:\FACULTAD\Todo python\Practica\practica.txt","w")
archivo.writelines(vec)
archivo.close

archivo = open("C:\FACULTAD\Todo python\Practica\practica.txt","r")
contenido = archivo.read()
print (contenido)
archivo.close

def contar_lineas (a, cam):  #contar cantidad de lineas que tiene el vector 
    c = 0
    a = open(cam, "r")
    for linea in a.readlines():
        c = c+1
    a.close()
    return c, a

def volcarvector (a, cam, x): #metemos todos los datos del archivo en un vector 
    i = 0
    a = open(cam, "r")
    linea = a.readline()
    while linea != "":
        x[i] = linea
        i += 1
        linea = a.readline()
    a.close()

def ordenar (x,n): #ordena los datos del vector
    for i in range (0,n-1):
        for j in range(i+1,n):
            if x[i]>x[j]:
                aux = x[i]
                x[i] = x[j]
                x[j] = aux

def mostrar (x,n):
    for i in range (n):
        print(x[i])

fil =""
ubi = "C:\FACULTAD\Todo python\Practica\practica.txt"
n, fil =contar_lineas(fil, ubi)
v = [None] * n
volcarvector (fil, ubi, v)
print("datos del vector luego de la lectura del archivo: ")
print("-------------------------")
mostrar(v,n)
print("-------------------------")
print("\n")
ordenar(v,n)
mostrar(v,n)





        