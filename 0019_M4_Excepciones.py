#Excepciones
#Son errores que ocurren durante la ejecución de un programa

#La rama try-except
#Permite manejar errores y continuar
#Ejemplo
print("La rama try-except")
try: #intenta hacer esto
    x = int(input("Ingresa un número: ")) #ingresa un número
    print ("El recíproco de", x, "es", 1/x) #imprime el recíproco del número
except: #si hay un error
    print ("Ups! Hubo un error, Chaoooo") #imprime el mensaje
print()

#Ejemplo dos excepciones después de un try
print("Ejemplo dos excepciones después de un try")
try: #intenta hacer esto
    x = int(input("Ingresa un número: ")) #ingresa un número
    print ("El recíproco de", x, "es", 1/x) #imprime el recíproco del número
except ValueError: #si hay un error de valor
    print ("Ups! Hubo un error, Chaoooo") #imprime el mensaje
except ZeroDivisionError: #si hay un error de división por cero
    print ("Ups! División por cero no está permitida")
print()

#Ejemplo de excepción predeterminada
print("Ejemplo de excepción predeterminada")
try: #intenta hacer esto
    x = int(input("Ingresa un número: ")) #ingresa un número
    print ("El recíproco de", x, "es", 1/x) #imprime el recíproco del número
except ValueError: #si hay un error de valor
    print ("Ups! Hubo un error, Chaoooo") #imprime el mensaje
except ZeroDivisionError: #si hay un error de división por cero
    print ("Ups! División por cero no está permitida")
except: #si hay un error
    print ("Algo salió mal")
print()

#print debugging (depuración)
#Es una técnica para encontrar errores en el código
#Ejemplo
print("Print debugging")
def division(x,y): #definir la función con dos parámetros 
    print("x =", x) #imprimir el valor de x
    print("y =", y) #imprimir el valor de y
    if y == 0: #si y es igual a 0
        print("Ups! División por cero no está permitida")
        return None
    print("x/y = ", x/y) #imprimir la división de x entre y
    return x/y #devuelve la división de x entre y

print(division(10,2))#llamar a la función
print(division(10,0))#llamar a la función
print()
#el print debugging en este caso imprime los valores de x y y y el resultado de la
#división de x entre y, y si y es igual a 0 imprime un mensaje de error
#esto nos ayuda a encontrar errores en el código y que todo sea más claro



