#Operadores de Cadena 
#Los operadores de cadena permiten realizar operaciones con cadenas de texto
#Ejemplo de concatenación de cadenas
nombre = input("Ingresa tu nombre: ") #permite ingresar un nombre
apellido = input("Ingresa tu apellido: ") #permite ingresar un apellido
print ("Gracias...")
print ("Tu nombre completo es: " + nombre + " " + apellido + "...\n") #imprime el nombre completo

#Ejemplo de multiplicación de cadenas
#dibujo de una cuadradito
print ("Dibujo de cuadradito")
print ("+" + 10 * "-" + "+") #imprime el diseño del primer lado
print (("|" + " " *10 + "|\n") * 6, end="") #imprime el diseño de los lados
print ("+" + 10 * "-" + "+") #imprime el diseño del último lado