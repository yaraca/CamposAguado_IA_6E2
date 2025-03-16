#Bucles
#Los bucles son estructuras de control que nos permiten repetir un segmento de código un determinado número de veces

#Bucle infinito while
#Un bucle infinito significa que el código se ejecutará sin detenerse, infinitamente.
# while True:
#     print("Hola")
#Para detener un bucle infinito se puede usar las teclas ctrl + c

#Bucle while
#El while se utiliza para repetir un bloque de código mientras una condición sea verdadera
#Ejemplo bucle While
print ("Ejemplo de bucle While")
valor_max = -999999999
num = int(input("Introduce un número o escribe -1 para detener: "))
while num != -1: #mientras num sea diferente de -1
    if num > valor_max: #si num es mayor que valor_max
        valor_max = num #valor_max adquiere el valor de num
    num = int(input("Introduce el número o escribe -1 para detener: "))
print("El número más grande es: ", valor_max) #imprime el número más grande 
print ()

#-------------------------------------------------------

#Ejemplo bucle While
#Números pares e impares
print ("Ejemplo numros pares e impares")
impar = 0 
par = 0
num = int(input("Introduce un número o escribe 0 para detener: "))
while num != 0: #mientras num sea diferente de 0
    if num % 2 == 1: #si el residuo de num entre 2 es igual a 1
        impar += 1 #impar se incrementa en 1
    else: #sino
        par += 1 #par se incrementa en 1
    num = int(input("Introduce un número o escribe 0 para detener: "))
print("Conteo de números Pares: ", par)
print("Conteo de números Impares: ", impar)
print ()

#-------------------------------------------------------

#Variable counter para salir de un bucle 
#Ejemplo counter
print ("Ejemplo de variable counter")
counter = 5 #el contador es igual a 5
while counter != 0: #mientras counter sea diferente de 0
    print ("Dentro del bucle...", counter)
    counter -= 1 #decrementa en 1
print ("Fuera del bucle...", counter)
print ()

#-------------------------------------------------------

#Ejercicio con bucle while
#Ejercicio 1 Número secreto 
print ("Ejemplo de número secreto")
numero_secreto = 2828
print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")
num = int(input("Introduce un número:"))
while num != numero_secreto: #mientras num sea diferente de numero secreto
    print("¡Ja, ja! ¡Estás atrapado en mi ciclo!")
    num = int(input("Introduce un número:"))
print("¡Bien hecho, muggle! Eres libre ahora") #cuando num sea igual a numero_secreto
print ()

#-------------------------------------------------------
#Ejemplo 2 break
print ("Ejemplo de sentencia break")
valor_max = -999999999
contador = 0
while True: #mientras sea verdadero
    num = int(input("Introduce un número o escribe -1 para finalizar el programa: "))
    if num == -1: #si num es igual a -1
        break #sale dle bucle
    contador += 1 #si no, incrementa en 1
    if num > valor_max: #si num es mayor que valor_max
        valor_max = num

if contador !=0: #si el contador es diferente de 0
    print ("El número más grande es: ", valor_max) #imprime el valor máximo
else: 
    print ("No se ha ingresado ningún número") #sino, imprime el mensaje
print ()

#-------------------------------------------------------

#Ejercicio con bucle while
#Chupacabras
print ("Ejemplo de chupacabras")
word = input("Introduce la palabra secreta: ")
while word != "chupacabra": #mientras word se diferente de chupacabra
    print ("Palabra incorrecta...")
    word = input("Introduce la palabra secreta: ")
print ("¡Has dejado el ciclo con éxito!") #cuando word sea igual a chupacabras, imprime
print ()

#-------------------------------------------------------
#While y el bloque else
#El bloque else se ejecuta cuando la condición del bucle es falsa
#Ejemplo de while y else
print ("Ejemplo de while y else")
i = 1
while i < 4: #mientras i sea menor que 4
    print ("Dentro del bucle...", i)
    i += 1 #incrementa en 1
else: #sino
    print ("Fuera del bucle...") #cuando i sea mayor o igual a 4 el bucle se hace falso
print ()

#-------------------------------------------------------
#Ejercicio con bucle while
#Ejercicio Bloques de madera
print ("Ejemplo de bloques de madera")
bloques = int(input("Introduce el número de bloques:"))
altura = 0
contador = 1
while contador <= bloques: #mientras contador sea menor o igual a bloques
    altura += 1 #incrementa en 1
    bloques -= contador #bloques es igual a bloques - contador
    contador += 1 #incrementa en 1
print ("La altura de la pirámide: ", altura) #imprime la altura de la pirámide
print ()

#-------------------------------------------------------

#Ejercicio con bucle while
#Ejercicio La hipótesis de Collatz
print ("Ejemplo de hipótesis de Collatz")
num = int(input("Introduce un número entero, que no sea negativo o cero: "))
while num <= 0: #mientras num sea menor o igual a 0
    num = int(input("Número inválido. Introduce un número entero positivo: "))
c0 = num 
pasos = 0
while c0 != 1: #mientras c0 sea diferente de 1
    if c0 % 2 == 0: #si el residuo de c0 entre 2 es igual a 0
        c0 = c0 // 2 #c0 es igual a c0 entre 2
    else:
        c0 = 3 * c0 + 1 #sino, c0 es igual a 3 por c0 más 1
    print (c0) #imprime c0
    pasos +=1 #incrementa en 1
print ("Pasos = ", pasos ) #imprime los pasos
print ()


