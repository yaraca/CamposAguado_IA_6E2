#Operadores de comparación
#Los operadores de comparación se utilizan para comparar dos valores

#Operador de igualdad (==)
#El operador == va a comparar dos valores y va a devolver True si son iguales y False si no lo son
print ("Operador de igualdad (==)")
a = 10
print (a == 10) #compara si a es igual a 10 (true)
print (a == 5) #compara si a es igual a 5 (false)

#Operador de desigualdad (!=)
print ("Operador de desigualdad (!=)")
b = 5
print (b != 10) #compara si b es diferente de 10 (true)
print (b != 5) #compara si b es diferente de 5 (false)

#Operador de mayor que (>)
print ("Operador de mayor que (>)")
c = 11
print (c > 10) #compara si c es mayor que 10 (true)
print (c > 15) #compara si c es mayor que 15 (false)

#Operador de mayor o igual que (>=)
print ("Operador de mayor o igual que (>=)")
d = 12
print (d >= 12) #compara si d es mayor o igual que 12 (true)
print (d >= 15) #compara si d es mayor o igual que 15 (false)

#Operador menor o igual que (<=)
print ("Operador de menor o igual que (<=)")
e = 13
print (e <= 13) #compara si e es menor o igual que 12 (true)
print (e <= 10) #compara si e es menor o igual que 15 (false)
print ()

#--------------------------------------------------

#Ejercicio Operadores de comparación 
#Ingresar un valor, imprimir False si es menor que 100, si es mayor o igual a 100 imprimir True
print ("Ejercicio Operadores de comparación")
x = int(input("Ingrese un valor: "))
print (x >= 100, ", mayor o igual que 100")