#Función input
#la función input() permite al usuario ingresar un valor
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