#Entradas y salidas simples
#Función input
# #la función input() permite al usuario ingresar un valor
print ("Ingresa tu nombre:") 
nombre = input() #asigna el nombre ingresado a la variable 
print ("Hola,", nombre,"!") #imprime el nombre ingresado
print ()

#Ejemplo de función input con float
numero = float(input("Ingresa un número: ")) #permite ingresar un número
num = numero + 20 #multiplica el numero ingresado por 20
print ("La suma del número ingresado más 20 es igual a:", num) #imprime el resultado de la suma
print ()

#Ejemplo de la función input con int (números enteros)
numero = int(input("Ingresa un número: ")) #permite ingresar un número
num = numero + 50 #suma el número ingresado más 50
print ("La suma del número ingresado más 50 es igual a:", num) #imprime el resultado de la suma
print ()

#Ejemplo obtener hipotenusa con la función input
a = float(input("Ingresa el valor del primer cateto: ")) #permite ingresar un número
b = float(input("Ingresa el valor del segundo cateto: ")) #permite ingresar un número
print ("El valor de la hipotenusa es: ", (a**2+b**2)**0.5) #imprime el valor de la hipotenusa 
print ()

#Ejercicio de las entradas y salidas simples
#Operaciones aritméticas básicas
print ("Calculadora básica...")
x = float(input("Ingresa el primer valor: ")) #ingresar el primer número
y = float(input("Ingresa el segundo valor: ")) #Ingresar el segundo valor
print ("La suma de los valores es: ", x + y) #Imprime la suma de los valores
print ("La resta de los valores es: ", x - y) #Imprime la resta de los valores
print ("La multiplicación de los valores es: ", x * y) #Imprime la multiplicación de los valores
print ("La división de los valores es: ", x / y) #Imprime la división de los valores
print ("Gracias por su preferencia...")