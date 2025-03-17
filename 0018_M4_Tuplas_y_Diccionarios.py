#Tuplas y diccionarios

#Tuplas
#Las tuplas y diccionarios son estructuras de datos que permiten almacenar varios elementos en una sola variable
#Las tuplas son inmutables, no se pueden modificar una vez creadas
#las listas se hacen con () y los diccionarios con {}

#Ejemplo de tuplas
print ("Ejemplo de tuplas")
tupla1 = (1,2,3,4,5) #crear una tupla
tupla2 = 6,7,8,9,10 #crear una tupla
print(tupla1) #imprimir tupla1
print(tupla2) #imprimir tupla2
print()

#Imprimir elementos de una tupla
print("Imprimir elementos de una tupla")
tupla = (1,10,15,26,30)
print(tupla) #imprimir la tupla
print(tupla[0]) #imprimir el primer elemento de la tupla
print(tupla[-1]) #imprimir el ultimo elemento de la tupla
print(tupla[1:]) #imprimir los elementos de la tupla a partir del segundo elemento
print(tupla[:-2]) #imprimir los elementos de la tupla menos los dos últimos 
print()

#Operaciones con tuplas
print("Operaciones con tuplas")
tupla = (1, 10, 100, 1000)
t1 = tupla + (10000, 100000) #concatenar tuplas
t2 = tupla * 3 #multiplicar tuplas
print(len(t2)) #imprimir la longitud de la tupla
print(t1) #imprimir la tupla concatenada
print (t2) #imprimir la tupla multiplicada
print (100 in tupla) #buscar un elemento en la tupla
print (-10 not in tupla) #buscar un elemento que no esta en la tupla
print()

#--------------------------------------------------

#Diccionarios 
#No son secuencias, son colecciones de pares clave-valor
#Las claves son únicas y los valores no

#Ejemplo de diccionarios 
print("Ejemplo de diccionarios")
diccionario = {"gato": "cat", "perro": "dog", "ratón": "mouse"} #crear un diccionario
numeros = {1: "uno", 2: "dos", 3: "tres"} 
vacio = {} #crear un diccionario vacio
print(diccionario) #imprimir el diccionario de palabras
print(numeros) #imprimir el diccionario de numeros
print(vacio) #imprimir el diccionario vacio
print(diccionario["gato"]) #imprimir el valor de la clave gato
print()

#Ejemplo diccionario español - inglés
print("Ejemplo diccionario español - inglés")
diccionario = {"gato": "cat", "perro": "dog", "ratón": "mouse"} #crear un diccionario
palabras = ["gato", "leon", "perro", "ratón"] #crear una lista de palabras
for palabra in palabras: #para cada palabra en la lista 
    if palabra in diccionario: #si la palabra esta en el diccionario
        print (palabra, "->", diccionario[palabra])
    else: #si no esta en el diccionario
        print(palabra, "no está en el diccionario")
print()

#Método keys()
#Este método devuelve una lista con las claves del diccionario
print("Método keys()")
diccionario = {"gato": "cat", "perro": "dog", "ratón": "mouse"} #crear un diccionario
for key in diccionario.keys(): #para cada clave en el diccionario
    print(key, "->", diccionario[key]) #imprimir la clave y el valor 
print()

#Método items()
#Este método devuelve una lista de tuplas con clave y valor
print("Método items()")
diccionario = {"gato": "cat", "perro": "dog", "ratón": "mouse"} #crear un diccionario
for español, ingles in diccionario.items(): #para cada clave y valor en el diccionario
    print(español, "->", ingles) #imprimir la clave y el valor
print()

#Modificar, agregar y eliminar valores de un diccionario
print("Modificar, agregar y eliminar valores de un diccionario")
diccionario = {"gato": "cat", "perro": "dog", "ratón": "mouse"} #crear un diccionario
diccionario["gato"] = "feline" #modificar el valor de la clave gato
diccionario["pescado"] = "fish" #agregar una nueva clave y valor al diccionario
print(diccionario) #imprimir el diccionario nuevo
del diccionario["ratón"] #eliminar la clave ratón del diccionario
print(diccionario) #imprimir el diccionario sin la clave ratón
diccionario.update({"pájaro": "bird", "serpiente": "snake"}) #agregar claves y valores con update()
print(diccionario) #imprimir el diccionario con las nuevas claves y valores
diccionario.popitem() #eliminar el último elemento del diccionario
print(diccionario) #imprimir el diccionario sin el último elemento
print()

#--------------------------------------------------

#Ejemplo de tuplas y diccionarios
print("Ejemplo de tuplas y diccionarios")
#Ejercicio promedios de alumnos
clase = {}
while True:
    nombre = input("Ingrese el nombre del alumno: ") #pedir el nombre del alumno
    if nombre == "": #si el nombre está vacio
        break #salir del bucle
    notas = int(input("Ingrese la calificación del alumno: "))
    if notas not in range (0, 11): #si la nota no está en el rango de 0 a 10
        print("La nota debe estar entre 0 y 10")
        continue
    if nombre in clase: #si el nombre del alumno está en la clase
        clase[nombre] += (notas,) #agregar la nota a la tupla
    else: #si el nombre no está en la clase
        clase[nombre] = (notas,) #agregar el nombre y la calificación a la clase

for nombre in sorted(clase.keys()): #para cada nombre en la clase ordenada
    sum = 0
    contador = 0
    for notas in clase[nombre]: #para cada calificación en la clase
        sum += notas #sumar las calificaciones
        contador += 1 #contar las calificaciones
    print(nombre, ":", sum/contador) #imprime el promedio de calificaciones
print()
