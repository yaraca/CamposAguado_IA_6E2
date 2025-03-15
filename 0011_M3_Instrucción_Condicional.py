#Instrucción condicional
#Las condiciones son expresiones que se pueden evaluar como verdaderas o falsas

#Condición if (si)
print ("Ejemplo de condición if")
a = 33
b = 200
if b > a: #si b es mayor que a
    print("b es mayor que a") #imprime el mensaje
print ()

#condifción if-else (si-sino)
print ("Ejemplo de condición if-else")
a = 200
b = 33
if b > a: #si b es mayor que a
    print("b es mayor que a") #imprime el mensaje
else: #sino
    print("b no es mayor que a") #imprim el segundo mensaje 
print ()

#Condicion if-else anidada (if dentro de otro if)
print ("Ejemplo de condición if-else anidada")
a = 200
b = 150
c = 30
if a > b: #si a es mayor que b
    if c > b: #y si c es mayor que b
        print("a y c son mayores que b")
    else:
        print("a es mayor que b, y b es mayor que c")
else:
    print("b es mayor que a")
print ()

#condición elif (de lo contrario, si)
print ("Ejemplo de condición elif")
a = 33
b = 33
if b > a: #si b es mayor que a
    print("b es mayor que a") #imprime el mensaje
elif a == b: #si a es igual a b 
    print("a y b son iguales") #imprime el mensaje
else: #sino
    print("a es mayor que b")
print ()

#--------------------------------------------------

#Ejemplo if-else
print ("Ejemplo de condición if-else")
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
if num1 > num2:
    print ("El número", num1, "es mayor que", num2)
else:
    print ("El número", num2, "es mayor que", num1)
print ()

#--------------------------------------------------

#Ejemplo if-if
print ("Ejemplo de condición if-if")
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
valor_max = num1 #se asume que el valor máximo es el primer número
if num2 > valor_max:
    valor_max = num2 #si el segundo número es mayor, se asigna a valor_max
if num3 > valor_max:
    valor_max = num3 #si el tercer número es mayor, se asigna a valor_max
print ("El número mayor es: ", valor_max)
print ()

#--------------------------------------------------

#Ejemplo extra: función max() y min()
print ("Ejemplo de función max() y min()")
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
print ("El número mayor es: ", max(num1, num2, num3))
print ("El número menor es: ", min(num1, num2, num3))
print ()

#--------------------------------------------------

#Ejercicio instrucciones condicionales
#Ejercicio 1 if-elif-else
#Flor favorita
flor = input("Ingresa el nombre de la flor: ")
if flor == "ESPATIFILO": #si la flor es ESPATIFILO
    print ("¡ESPATIFILO es la mejor planta de todas!") #imprime el mensaje
elif flor == "espatifilo": #si la flor es espatifilo
    print ("No, ¡quiero un gran Espatifilo!") #imprime el mensaje
else: #sino es ninguna de las anteriores
    print ("¡Espatifilo! ¡No", flor + "!") #imprime el mensaje

#--------------------------------------------------

#Ejercicio instrucciones condicionales
#Ejercicio 2 if-else
#Calculadora de impuestos
ingreso = float(input("Introduce el ingreso anual: "))
if ingreso < 85528: #si el ingreso es menor a 85528
    impuesto = (ingreso * 0.18) - 556.02 #calcula el impuesto 
else:
    impuesto = 14839.02 + ((ingreso - 85528)* 0.32) #calcula el impuesto
if impuesto < 0: #si el impuesto es menor que 0
    impuesto = 0.0 #se le asigna el valor de 0
impuesto = round(impuesto, 0) #redondea el valor del impuesto a pesos totales
print ("El impuesto es: ", impuesto, "pesos")
print ()

#--------------------------------------------------

#Ejercicio instrucciones condicionales
#Ejercicio 3 if-elif-else
#Año bisiesto
año = int(input("Introduce un año: "))
if año < 1582: #si el año es menor qu e1582
    print ("NO esta dentro del periodo del calendario gregoriano")
elif año % 4 != 0: #si el año no es divisible entre 4
    print ("Es un año común")
elif año % 100 != 0: #si el año no es divisible entre 100
    print ("Es un año bisiesto")
elif año % 400 != 0: #si el año no es divisible entre 400
    print ("Es un año común")
else: #sino
    print ("Es un año bisiesto")
