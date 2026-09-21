""" #Declarando un arreglo 
numeros = [10,20,30,40,50]

#Imprimos un elemento especifico del arreglo
print(numeros[2])

#Reasignamos un elemento a un nuevo valor
numeros[3] = 35
print(numeros)

#Agrega un nuevo valor al final del arrglo
numeros.append(60)
print(numeros)

#Eliminamos un valor en el arrglo
numeros.remove(35)
print(numeros)

#Eliminamos un valor del arreglo usando la posición
numeros.pop(4)
print(numeros)


frutas = ["Manzana","Fresa","Sandia","Mango","Melon","Platano"]
frutas.pop(4)
print(frutas)

frutas.remove("Manzana")
print(frutas)

arreglo = []
print(arreglo)

n = int(input("Ingrese el tamaño del arreglo: "))

for i in range(n):
    dato = int(input("Ingrese un numero: "))
    arreglo.append(dato)

print("El arreglo es: " , arreglo)

arreglo1 = []
n1 = int(input("Anota el tamaño del arreglo: "))

for i in range (n1):
    dato1 = int(input("Ingrese un numero: "))
    arreglo1[i] = dato1

print(arreglo1) """

numeros = []

for i in range (15):
    num = int(input("Ingresa el numero: "))
    numeros.append(num)

cincue = numeros.copy()

for i in range (15):
    if cincue[i] % 5 != 0:
        cincue[i] = cincue[i] + (5-cincue[i]%5)

print("\n Arreglo brrOriginal")
print(numeros)

print("\n Arreglo brrCincuerizado")
print(cincue)

