#Bucle For 
#El bucle for se utiliza para iterar sobre una secuencia, sea una lista, tupla, conjunto, cadena, etc.
#Ejemplo bucle For
print ("Ejemplo de bucle For")
for i in range (10): #para i en el rango de 0 a 9
    print ("El valor de i es: ", i) #imprime el valor de i
#la función range() genera una secuencia de números
#esta función solo acepta enteros como argumentos, puede usar 1, 2 o 3 argumentos
#si se usa un argumento, range(n) genera una secuencia de números desde 0 hasta n-1
#cuando tiene 2 argumentos n, m, genera una secuencia de números desde n hasta m-1
#cuando tiene 3 argumentos n, m, s, genera una secuencia de números desde n hasta m-1 con un paso s
print ()

#-------------------------------------------------------
#Ejemplo bucle for, con range de 3 argumentos
print ("Ejemplo de bucle For con range de 3 argumentos")
for i in range (2, 15, 3): #para i en el rango de 2 a 14 con un paso de 3
    print ("El valor de i es: ", i) #imprime el valor de i
print ()

#-------------------------------------------------------
#Ejemplo bucle for Exponentes
print ("Ejemplo de bucle For Exponentes")
res = 1
for exponente in range (5): #para exponente en el rango de 0 a 13
    print ("3 elevado a la", exponente, "es igual a", res) #imprime el valor de 3 elevado a una exponente
    res *= 3 #el resultado se multiplica por 3
print()

#-------------------------------------------------------

#Ejercicio de bucle for
#Ejercicio 1 Contando lentamente Mississipily
import time #importa la libreria time
for i in range (1, 6): #para i en el rango de 1 a 5
    print (i, "Mississippi") #imprime el valor de i y la palabra mississipi
    time.sleep(1) #detiene el programa por 1 segundo
print ("¡Listos o no, ahí voy!") #cuando termina el bucle, imprime el mensaje 
print ()

#-------------------------------------------------------
#Sentencias break y continue
#La sentencia break se utiliza para salir de un bucle
#La sentencia continue se utiliza para saltar a la siguiente iteración de un bucle
#Ejemplo break
print ("Ejemplo de sentencia break")
print ("La instrucción break: ")
for i in range (1, 11): #para i en el rango de 1 a 10
    if i == 6: #si i es igual a 6
        break #sale del bucle
    print ("Dentro del bucle...", i)
print ("Fuera del bucle...") #cuando termina el bucle, imprime el mensaje
print ()

#Ejemplo continue
print ("Ejemplo de sentencia continue")
print ("La instrucción continue: ")
for i in range (1,7): #para i en el rango de 1 a 6
    if i == 3: #si i es igual a 3
        continue #salra a la siguiente iteración
    print ("Dentro del bucle...", i)
print ("Fuera del bucle...") #cuando termina el bucle, imprime el mensaje
print ()

#-------------------------------------------------------

#Ejercicio de bucle for
#El feo devorando vocales
print ("Ejercicio de bucle for")
palabra = input("Ingresa una palabra: ")
palabra = palabra.upper() #convierte la palabra a mayúsculas
for i in range (len(palabra)): #para i en el rango de la longitud de la palabra
    if palabra[i] in "AEIOU": #si la letra de la palabra en la posición i esta en AEIOU
        continue
    print (palabra[i]) #imprime la letra
else:
    print ("Fin del programa")
print ()

#-------------------------------------------------------
#For y bloque else
#El bloque else se ejecuta cuando el bucle termina de iterar sobre la lista
#Ejemplo de bloque else
print ("Ejemplo de bloque else")
for i in range (5): #para i en el rango de 0 a 4
    print (i) #imprime el valor de i
else: #cuando termina el bucle
    print ("Fin del programa...")
print ()


