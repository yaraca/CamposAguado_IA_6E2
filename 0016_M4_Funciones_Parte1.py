#Funciones
#Una función es un bloque de código que solo se ejecuta cuando se llama

#Ejemplo de función 
print ("Ejemplo de función")
def mensaje(): #definir la función
    print("Ingresa valor: ")

print("Inicia aquí")
mensaje() #llamar la función
print("Termina aquí")
print()

#Ejemplo de función 
print ("Ejemplo de función")
def mensaje2(): #deifnir la función
    print ("Ingresa valor: ")
mensaje2() #llamar la función
a= int(input())
mensaje2() #llamar la función
b = int(input())
mensaje2()
c = int(input())
print("La suma es: ", a+b+c)
print()

#Ejemplo de función con argumentos
print ("Ejemplo de función con argumentos")
def hola(nombre): #definir la función con argumento 
    print("Hola", nombre) 
nombre = input("Ingresa tu nombre: ")
hola(nombre)#llamar la función con la entrada del usuario
print()

#--------------------------------------------------

#Funciones parametrizadas
#Ejemplo función con 2 parámetros
print ("Ejemplo de función con 2 parámetros")
def mensaje3(que, numero): #definir la función con 2 parámetros
    print ("Ingresa", que, "número", numero)

mensaje3("telefono", 1) #llamar la función con 2 argumentos
mensaje3("casa", 4)
mensaje3("precio", 10)
print()

#Parámetros posicionales 
#Ejemplo función con parámetros posicionales
print ("Ejemplo de función con parámetros posicionales")
def presentacion(nombre, apellido): #definir la función con 2 argumentos 
    print ("Hola, mi nombre es", nombre, apellido)

presentacion("Yara", "Campos") #llamar la función con 2 argumentos
print()

#Ejemplo argumentos posicionales y de palabras clave
print ("Ejemplo de argumentos posicionales y de palabras clave")
def operacion(a,b,c): #definir la función con 3 argumentos 
    print (a, "+", b, "+", c, "=", a+b+c)
operacion(1,2,3)
print()

#--------------------------------------------------
#Función con retorno
#Estas funciones devuelven un valor que puede ser utilizado en otra parte del programa
#Ejemplo de función con retorno
print ("Ejemplo de función con retorno")
def año_nuevo(cuenta = True): #definir la función con un parámetro
    print("Tres...")
    print("Dos...")
    print("Uno...")
    if not cuenta:
        return
    print("Feliz año nuevo!")

año_nuevo() #llamar la función
año_nuevo(False) #llamar la función con el parámetro False
print()

#Ejemplo de función con retorno con una expresión
print ("Ejemplo de función con retorno con una expresión")
def funcion(): #definir la función
    return 5*5
x = funcion() #llamar la función y darl el valor de retorno a x
print("El resultado devuelto es: ", x)
print()

#--------------------------------------------------

#Listas y funciones
#Ejemplo de función con listas
print ("Ejemplo de función con listas")
def suma_lista(lista): #definir la función con un parámetro
    suma = 0
    for i in lista:
        suma += i #suma los elementos de la lista
    return suma #devuelve la suma
print("La suma de la lista es: ", suma_lista([5,10,15])) #imprime la suma de la lista
print()

#--------------------------------------------------

#Ejercicio de funciones 
#Son tres ejercicios que utilizan las mismas funciones
#Ejercicio Año bisiesto 
print ("Ejercicio Año bisiesto")
#función bisiesto
def bisiesto(año): #definir la función con un parámetro
    if año % 4 != 0: #si el año no es divisible entre 4
        return False #devuelve falso
    elif año % 100 != 0: #si el año no es divisible entere 100
        return True #devuelve verdadero
    elif año % 400 != 0: #si el año no es divisible entre 400
        return False #devuelve verdadero
    else:
        return True

datos = int(input("Ingresa el año: ")) 
if bisiesto(datos): #llamar la función
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")
print()


#Ejercicio Cúantos días hay en un mes
#Utiliza la función bisiesto y crea la función dias_en_mes
print ("Ejercicio Cúantos días hay en un mes")
def días_en_mes(año, mes): #definir la función con entrada de mes y año
    if not 1 <= mes <= 12 and año > 0: #si el mes no está entre 1 y 12 y el año es mayor a 0
        return None
    dias_x_mes = [31,28,31,30,31,30,31,31,30,31,30,31] #lista de días por mes
    if mes == 2 and bisiesto(año): #si el mes es febrero y el año es bisiesto
        return 29 #devuelve 29 dias
    return dias_x_mes[mes-1] #devuelve los días del mes correspondientes

año = int(input("Ingresa el año: "))
mes = int(input("Ingresa el mes: "))
dias = días_en_mes(año, mes) #llamar la función 
if dias == None:
    print ("Datos incorrectos")
else: 
    print("El mes", mes, "tiene", dias, "días")
print()


#Ejercicio Día del año 
#Utiliza la función bisiesto, la función dias_en_mes y crea la función dias_del_año
print ("Ejercicio Día del año")
def dia_del_año(año, mes, dia): #definir la función con entrada de año, mes y día
    dias_mes = días_en_mes(año, mes) #llamar la función días_en_mes
    if dias_mes is None or not 1 <= dia <= dias_mes: #si los días del mes son nulos o el día no está entre 1 y los días del mes
        return None #devuelve nulo
    
    total = sum(días_en_mes(año, m) for m in range(1, mes)) + dia #suma los días de los meses anteriores y el día 
    return total 

año = int(input("Ingresa el año: "))
mes = int(input("Ingresa el mes: "))
dia = int(input("Ingresa el día: "))
dias = dia_del_año(año, mes, dia) #llamar la funcion 
if dias is None:
    print("Datos incorrectos")
else: 
    print("El día", dia, "del mes", mes, "del año", año, "es el día", dias, "del año")
print()

#--------------------------------------------------

#Ejercicio de funciones 
#Ejercicio Números primos 
print ("Ejercicio Números primos")
def num_primo(num): #definir la función 
    for i in range(2, int(1 + num ** 0.5)): #para i en el rango de 2 a la raíz cuadrada de num
        if num % i == 0: #si num es divisible entre i
            return False
        return True
print("Los números primos del 1 al 15 son:")
for i in range(1, 15): #para i en el rango de 1 al 15
    if num_primo(i+1): #llamar la función 
        print(i+1, end=" ")
print()

#--------------------------------------------------

#Ejercicio de funciones
#Ejercicio COnversión del consumo de combustible
print ("Ejercicio Conversión del consumo de combustible")
#1 milla = 1609.344 metros
#1 galón = 3.785411784 litros
#Escribir funciones que convierta 1/100 km a millas por galón y viceversa
def litros_100km_millas(litros): #definir la función de litros a 100 km a millas por galón
    galones = litros / 3.785411784 #litros a galones
    millas = 100 *1000 / 1609.344 #100 km a millas
    return millas / galones #devuelve la conversión 

def millas_litros_100km(millas): #definir la función de millas por galón a litros a 100 km
    km = millas * 1609.344 /1000 / 100 #millas a km
    litros = 3.785411784 #galones a litros 
    return litros / km #devuelve la conversión 

print("La conversión de 3.9 litros a 100 km a millas por galón es: ", litros_100km_millas(3.9)) #llamar la función 
print("La conversión de 60 millas por galón a litros a 100 km es: ", millas_litros_100km(60))
print()
