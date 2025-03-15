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
counter = 5 #el contador es igual a 5
while counter != 0: #mientras counter sea diferente de 0
    print ("Dentro del bucle...", counter)
    counter -= 1 #decrementa en 1
print ("Fuera del bucle...", counter)
print ()

#-------------------------------------------------------

#Ejercicio con bucle while
#Ejercicio 1 Número secreto 
numero_secreto = 777
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
print("¡Bien hecho, muggle! Eres libre ahora")