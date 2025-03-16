#Listas
#Las listas son un tipo de datos que nos permite almacenar varios valores en  una misma variable
#Las listas se definen con corchetes []
#Los elementos de una lista se separan por comas
#Los elementos siempre estan numerados desde el 0

#Indexación de listas
#Seleccionar un elemento de una lista
#Ejemplo indexación de listas
print ("Ejemplo de listas")
num = [10, 5, 7, 2, 1] #lista de numeros
print ("Contenido de la lista: ", num) #imprime la lista
num[0] = 111 #modifica el primer elemento de la lista y cambia su valor
print ("Lista modificada: ", num)#imprime la lista modificada
num [1] = num [4] #cambia el valor del segundo elemento por el ultimo
print ("Lista modificada: ", num)
print (num[0]) #imprime solo el primer elemento de la lista
print ("Longitud de la lista: ", len(num)) #imprime la longitud de la lista
print (num) #imprime la lista completa

#Eliminar elementos de una lista (del)
del num[1] #elimina el segundo elemento de la lista
print (len(num)) #imprime la longitud de la lista
print (num) #imprime la lista nueva
print (num[-1]) #imprime el ultimo elemento de la lista
print (num[0:3]) #imprime los elementos desde 0 hasta 3
print (num[1:]) #imprime los elementos desde 1 hasta el final
print ()

#-------------------------------------------------

#Ejercicio Listas
#Ejercicio sombrerero
print ("Ejercicio sombrerero")
num = [1, 2, 3, 4, 5] #lista de numeros
print ("Lista original: ", num)
new_num = int(input("Ingrese un número: "))
num [2] = new_num #cambia el valor del tercer elemento por el nuevo número
print ("Nueva lista: ", num)
del num[4] #elimina el último elemento de la lista
print ("Lista sin el último elemento: ", num)
print ("Longitud de la lista: ", len(num))
print ()

#-------------------------------------------------

#Agregar elementos a una lista (append(), insert())
#append() agrega un elemento al final de la lista
#insert() agrega un elemento en la posición que se le indique
#list.append(elemento)
#list.insert(posición, elemento)
#Ejemplo append, insert
print ("Ejemplo append, insert")
num = [1, 2, 3, 4, 5] #lista de numeros
print (num)
print (len(num))
num.append(6) #agregar el número 6 al final de la lista
print (num)
print (len(num))
num.insert(2, 7) #agregar el 7 en la posición 2 de la lista
print (num)
print (len(num))
print ()

#-------------------------------------------------
#Lista vacia + for
print ("Lista vacia + for")
num = [] #lista vacia
for i in range(5): #ciclo for de 5 elementos
    num.append(i+1) #agregar los elementos a la lista
print (num)
print ()

#-------------------------------------------------
#suma de elementos de una lista
print ("Suma de elementos de una lista")
num = [10, 20, 30, 40, 50] #lista de numeros
print (num)
suma = 0
for i in range(len(num)): #ciclo for en rango de la longitud de la lista
    suma += num[i] #suma de los elementos de la lista
print ("Suma de los elementos de la lista: ", suma)
print ()

#-------------------------------------------------
#Intercambiar elementos de una lista
print ("Intercambiar elementos de una lista")
num = [10, 20, 30, 40, 50] #lista de numeros
print (num)
num [0], num [4] = num [4], num [0] #intercambia el primer y ultimo elemento de la lista
print (num)
print ()

print ("Intercambiar elementos de una lista con For")
for i in range (len(num)//2): #ciclo for en rango de la longitud de la lista
    num[i], num[len(num)-i-1] = num[len(num)-i-1], num[i] #intercambia los elementos de la lista de un extremo al otro
print (num)
print ()  

#-------------------------------------------------
#Ejercicio Listas
#Ejercicio Los Beatles
print ("Ejercicio Los Beatles")
beatles = []
print ("Paso 1:", beatles)
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print ("Paso 2: ", beatles)
for i in range(2): #ciclo for de 2 elementos
    beatles.append(input("Ingrese el nombre de un integrante más: "))
print ("Paso 3: ", beatles)
del beatles[3] #eliminar el cuarto elemento de la lista
del beatles[3] #eliminar el quinto elemento de la lista
print ("Paso 4: ", beatles)
beatles.insert(0, "Ringo Starr") #agregar a Ringo Starr en la posición 0
print ("Paso 5: ", beatles)
print()

#-------------------------------------------------
#Ordenar elementos de una lista
#Ejemplo para ordenar elementos de una lista
print ("Ordenar elementos de una lista")
num = [ 8, 10, 6, 2, 4] #lista de números 
print (num)
swapped = True 
while swapped: #mientras swapped sea verdadero
    swapped = False #swapped es falso
    for i in range(len(num) - 1): #ciclo for en rango de la longitud de la lista -1
        if num[i] > num[i+1]: #si el elemento i es mayor al siguiente
            swapped = True
            num[i], num[i+1] = num[i+1], num[i] #intercambia los elementos 
print (num)
print()

#-------------------------------------------------
#Ordenamiento de burbuja 
#Ejemplo de ordenamiento de burbuja
print ("Ordenamiento de burbuja")
lista = []
swapped = True 
num = int(input("¿Cuántos elementos desea ordenar?..."))
for i in range(num): #ciclo for de la cantidad de elementos ingresados
    valor = float(input("Ingrese un elemento de la lista: "))
    lista.append(valor) #agregar los elementos a la lista

while swapped: 
    swapped = False
    for i in range (len(lista) - 1): #ciclo for en rango de la longitud de la lista -1
        if lista[i] > lista[i+1]: #si el elemento i es mayor que el siguiente
            swapped = True #el cambio va a ser verdadero
            lista[i], lista[i+1] = lista[i+1], lista[i] #intercambio de elementos 
print ("Lista ordenada: ", lista)
print()

#-------------------------------------------------
#Ordenar con sort()
#Este método ordena los elementos de una lista de menor a mayor
#Ejemplo de sort()
print ("Ordenar con sort()")
num = [8, 10, 6, 2, 4]
print ("Lista original: ", num)
num.sort() #ordena los elementos de la lista
print ("Lista ordenada: ", num)
print()