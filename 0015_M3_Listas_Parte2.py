#Operaciones con listas

#Rebanadas
#Las rebanadas son una forma de acceder a una parte de una lista
#Se especifica un rango de índices separados por dos puntos
#Ejemplo: lista[inicio:fin]
print ("Ejemplo de rebanadas copiando lista completa")
lista1 = [1]
print("Lista 1: ", lista1)
lista2 = lista1[:]#copia la lista completa
lista1[0] = 2 #modifica el primer elemento de la lista 1
print("Lista 2: ", lista2)
print("Lista 1 modificada: ", lista1)
print()

print("Ejemplo de rebanadas con rango")
lista = [1,2,3,4,5,6]
print("Lista original: ", lista)
new_lista = lista[1:4] #copia los elementos de las posiciones 1 a 3
print("Nueva lista: ", new_lista)
print()

#----------------------------------------------------
#Eliminar más de un elemento de la lista (del)
#del lista[inicio:fin]
#Ejemplo 
print("Eliminar más de un elemento de la lista")
lista = [1,2,3,4,5]
print("List: ", lista)
del lista[1:3] #elimina los elementos de las posiciones 1 y 2
print("Lista modificada: ", lista)
print()

#----------------------------------------------------
#Operadores in y not in
#permiten verificar si un elemento está o no en una lista
print("Operadores in y not in")
lista = [1,2,3,4,5]
print("Lista: ", lista)
print (8 in lista) #comprueba si 8 está en la lista (False)
print (3 in lista) #comprueba si 3 está en la lista (True)
print (8 not in lista) #comprueba si 8 no está en la lista (True)
print()

#----------------------------------------------------
#Ejercicio de Listas
#Ejecicio eliminar elementos repetidos de una lista
print("Ejercicio eliminar elementos repetidos de una lista")
lista = [1,2,3,4,4,1,5,6,6,2]
print("Lista original: ", lista)
new_lista = []
for i in lista:
    if i not in new_lista:
        new_lista.append(i)
print("Lista sin elementos repetidos: ", new_lista)
print()

#----------------------------------------------------

#Listas dentro de listas
#Ejemplos de listas dentro de listas
print("Listas dentro de listas")
cuadrados = [x ** 2 for x in range (10)] #Crea una lista con los cuadrados de los números del 0 al 9
print("Lista de cuadrados: ", cuadrados)
print()
dos = [2 ** i for i in range (8)] #crea una lista con las potencias de 2
print("Lista de potencias de 2: ", dos)
print()
impar = [ x for x in cuadrados if x % 2 != 0] #Crea una lista con los números impares de la lista de cuadrados
print("Lista de números impares: ", impar)
print()
