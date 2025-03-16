#Funciones Multiparamétricas

#Ejemplo de función con múltiples parámetros
#Ejemplo Cálculo de IMC
print("Calculo de IMC")
def imc(peso, altura): #definir la función con la entrada de peso y de altura
    if altura < 1.0 or altura > 2.5 or peso <20 or peso > 200: #condicionar la función
        return None #regresa un valor nulo
    return peso / altura ** 2 #calcular el IMC

def lb_kg(lb): #definir la función para convertir libras a kg
    return lb * 0.45359237 

def ft_in_m(ft, inch): #definir la función para convertir pies y pulgadas a mtrs
    return ft * 0.3048 + inch * 0.0254

print (imc(55, 1.65)) #llamar a la función con los valores de peso y altura
print (imc(320, 1.65)) #llamar a la función con los valores incorrectos
print (imc(peso = lb_kg(176), altura = ft_in_m(5, 7))) #llamar a la función con los valores en libras y pies
print()

#--------------------------------------------------

#Ejemplo Triángulos
print("Triángulos")
def triangulo (a,b,c): #definir la función con los lados del triángulo
    if a + b <= c: #si la suma de a y b es menor o igual que c
        return False #no es un triángulo
    if b + c <= a: #si la suma de b y c es menor o igual que a
        return False #no es un triángulo
    if c + a <= b: #si la suma de c y a es menor o igual que b
        return False #no es un triángulo
    return True #todo lo demás es un triángulo

print(triangulo(3,4,5)) #llamar a la función (True)
print(triangulo(3,4,7)) #llamar a la función (False)
print()

#Triángulos y teorema de pitágoras
print("Triángulos y teorema de pitágoras")
def pitagoras(a,b,c): #definir la función con los lados del triangulo
    if not triangulo(a,b,c): #si no es un triángulo
        return False 
    if c > a and c > b: #si c es mayor que a y b
        return c**2 == a**2 + b**2 #pitagoras
    if a > b and a > c:
        return a**2 == b**2 + c**2 #pitagoras
    if b > a and b > c:
        return b**2 == a**2 + c**2 #pitágoras
print(pitagoras(5,3,4)) #llamar a la función True
print(pitagoras(1,3,4)) #llamar a la función False
print()

#Área de un triángulo (formula de Herón)
print("Área de un triángulo")
def heron(a,b,c): #definir la función
    p = (a+b+c)/2 #calcular el semiperímetro
    return (p * (p-a) * (p-b) * (p-c)) ** 0.5 #calcular el área

def area_triangulo(a,b,c): #definir la función 
    if not triangulo(a,b,c): #si no es un triangulo
        return None
    return heron(a,b,c) #si es un triangulo calcular su area

print (area_triangulo(3,4,5))#llamar a la función 
print()

#--------------------------------------------------
#Ejemplo Factoriales
print("Factoriales")
def factorial(num): #definir la función con el número 
    if num < 0: #si el numero es menor que 0
        return None
    if num < 2: #si el numero es menor que 2
        return 1
    producto = 1
    for i in range (2, num + 1): #para i en el rango de 2 al número + 1
        producto *= i #multiplicar el producto por i
    return producto 

for num in range(1,7): #para num en el rango de 1 a 7
    print(num, factorial(num)) #imprimir el número y el factorial
print()

#--------------------------------------------------
#Ejemplo Fibonacci
print("Fibonacci")
def fib(n): #definir la función con el número
    if n < 1: #si el numero es menor que 1
        return None
    if n < 3: #si el numero es menor que 3
        return 1
    elem1 = elem2 = 1
    sum = 0
    for i in range (3, n + 1): #para i en el rango de 3 al numero + 1
        sum = elem1 + elem2 #sumar los elementos
        elem1, elem2 = elem2, sum #intercambiar los elementos 1 y 2
    return sum #regresa la suma

for n in range(1,10): #para i en el rango de 1 al 10
    print(n, "->", fib(n)) #imprimir el número y el fibonacci
print()