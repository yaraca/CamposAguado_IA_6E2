#Operadores Abreviados
#Los operadores abreviados permiten realizar operaciones aritméticas de manera más rápida
print ("Ejemplos de operadores abreviados...")
x = 5
x = x * 3 #multiplica el valor de x por 3
print ("El primer valor de x es:", x)
x *= 3 #multiplica el nuevo valor de x por 3
print ("El segundo valor de x es:", x)

y = 10
y/=2 #divide el valor de y entre 2
print ("El primer valor de y es:", y)
z = 1
z += 2 * y #suma el valor de z más 2 veces el valor de y 
print ("El resultado de z + 2*y es:", z)
print ()

#------------------------------------------------------------

#Ejercicio de operadores abreviados 1
#1 millas es aprox 1.61 km
print ("Ejercicio de operadores abreviados")
km = 12.25
millas = 7.38
conversion = 1.61

millas_a_km = millas * conversion #convierte millas a km
km_a_millas = km / conversion #convierte km a millas

print (millas, "millas son:", round(millas_a_km, 2), "km") #imprime el resultado de la conversión a km
print (km, "kilómetros son:", round(km_a_millas, 2), "millas") #imprime el resultado de la conversión a millas
#round(variable, decimales) redondea el valor de la variable a los decimales que se le indiquen
print()

#------------------------------------------------------------

#Ejercicios de operadores abreviados 2
#Solución de ecuación cubica
print ("Ejercicio de operadores abreviados 2")
print ("3x^3 - 2x^2 + 3x - 1")
x = 0
x = float(x)
y = 3*x**3 - 2*x**2 +3*x - 1 #ecuación cubica
print ("->Cuando X es igual a: ", x, "\nEl resultado (y) es: ", y) #imprime el resultado de la ecuación 
print ()

x = 1
x = float(x)
y = 3*x**3 - 2*x**2 +3*x - 1 #ecuación cubica
print ("->Cuando X es igual a: ", x, "\nEl resultado (y) es: ", y) #imprime el resultado de la ecuación 
print ()

x = -1
x = float(x)
y = 3*x**3 - 2*x**2 +3*x - 1 #ecuación cubica
print ("->Cuando X es igual a: ", x, "\nEl resultado (y) es: ", y) #imprime el resultado de la ecuación 
print ()

#------------------------------------------------------------

#Ejercicio Final Operadores Abreviados
#Evaluar operación aritmética
print ("Ejercicio Final de operadores abreviados!")
print ("Resolver la siguiente operación: 1/(a + 1/(a + 1/(a + 1/a)))")
a = float(input("Ingrese el valor de a: ")) #ingresa un número 
b = 1 / (a + 1 / (a + 1 / (a + 1 / a)))
print ("El resultado de la operación es: ", b) #imprime el valor de la operación 
