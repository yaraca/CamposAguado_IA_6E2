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
print ()

#Ejercicio Final Operadores y expresiones
print ("Ejercicio final de operadores y expresiones")
print ("¿A qué hora temina mi evento?...")
hora = int(input("Ingresa la hora de inicio (horas): "))
min = int(input("Ingresa los minutos de inicio (minutos):  "))
duracion = int(input("Ingresa la duración del evento (minutos): "))
min2 = min + duracion #suma los minutos de inicio más la duracion del evento
hora2 = hora + min2 // 60 #suma la hora de inicio más los minutos totales
min2 = min2 % 60 #calcula los minutos restantes
hora2 = hora2 % 24 #calcula las horas restantes
print ("El evento se termina a las... ", hora2, ":", min2, sep='')

