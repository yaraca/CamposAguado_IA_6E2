#Operadores Abreviados
x = 5
x = x * 3 #multiplica el valor de x por 3
print (x)
x *= 3 #multiplica el nuevo valor de x por 3
print (x)
print ()

y = 10
y/=2 #divide el valor de y entre 2
print (y)
z = 1
z += 2 * y #suma el valor de z más 2 veces el valor de y 
print (z)
print ()

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


