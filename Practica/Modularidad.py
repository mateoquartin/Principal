def mult(m):
    for i in range (10):
        print (m ,"x", i+1, "=" ,m*(i+1))

while True:
    x = int(input("ingresar la tabla de que numero generar: "))
    mult(x)
    print ("desea salir? si o no")
    s = input()
    if s == "si":
        break

def primo (numero):
    cc = 0
    for i in range (2, numero):
        if (numero % i)==0:
            cc +=1
    if cc == 0:
        return True
    else:
        return False
n = int(input("ingresar la cantidad de numeros para contar cuantos son primos"))
c = 0
for i in range (n):
    numerop = int(input(f"ingresa el numero {i+1}: "))
    if primo (numerop) == True:
        c +=1
print (f"la cantidad de primos es:{c}")


