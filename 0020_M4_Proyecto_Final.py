#Tic-Tac-Toe
#Juego de gato


from random import randrange #importamos la función randint de la libreria random
import time #importamos la libreria time

def diseño_tablero(tablero): #definir la función tablero
    print("+-------" * 3, "+", sep="") #imprimir el tablero
    for fila in range(3): #para fila en el rango de 3
        print("|       " * 3, "|", sep="")
        for columna in range(3): #para columna en el rango de 3
            print("|   " + str(tablero[fila][columna]) + "   ", end="") #imprimir el tablero
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")

def jugada(tablero): #definir la función jugada 
    ok = False
    while not ok:
        movimiento = input("\nIngresa tu movimiento: ")#pedir el movimeinto del jugador
        ok = movimiento.isdigit() and 1 <= int(movimiento) <= 9 #si el movimiento es un número y está entre 1 y 9
        if not ok: #si no es correcto
            print("Movimiento incorrecto, intentalo de nuevo")
            continue
        movimiento = int(movimiento) -1 #convertir el movimiento a entero y restarle 1
        fila, columna = movimiento // 3, movimiento % 3 #calcular la fila y columna
        if tablero[fila][columna] in ["O", "X"]: #si la posición del tablero es O o X
            print("Casilla ocupada, intentalo de nuevo")
            ok = False #no es correcto 
            continue
        tablero[fila][columna] = "O" #la posición del tablero es O 
        break

def campos_libres(tablero): #definir la función de campos libres en el tablero
    libre = [(fila, columna) for fila in range (3) for columna in range (3) if tablero[fila][columna] not in ["O", "X"]] #calcular los campos libres
    return libre #devolver los campos libres

def ganador(tablero, signo): #definir la función ganadora 
    quien = "yo" if signo == "X" else "tu" #si signo es X entonces yo sino tu
    for filacolumna in range (3): #para fila y columna en el rango de 3
        if all (tablero[filacolumna][i] == signo for i in range (3)) or all (tablero[i][filacolumna] == signo for i in range (3)): #si todas las filas y columnas son iguales a buscar
            return quien #devolver quien
    if all (tablero[i][i] == signo for i in range(3)) or all (tablero[i][2-i] == signo for i in range(3)): #si todas las diagonales son iguales a signo
        return quien #devolver quien
    return None #devolver nulo

def movimiento_computadora(tablero): #definir la función dibujar movimiento
    libre = campos_libres(tablero) #calcular los campos libres 
    if libre: 
        print("Pensando...")
        time.sleep(3) #esperar 3 segundos
        fila, columna = libre[randrange(len(libre))] #calcular la fila y columna aleatoria
        tablero[fila][columna] = "X" #la posición del tablero es X


print("\n-------JUEGO de GATO-------\n")
print("Tú eres 'O' y yo soy 'X'")
print("Las casillas están numeradas del 1 al 9\n")
print("Mucha Suerteee <3")
print("El tablero es el siguiente...\n")
time.sleep(2) #esperar 2 segundos
tablero = [[3 * j + i + 1 for i in range(3)] for j in range(3)] #crear el tablero
tablero[1][1] = "X" #posición del jugador
jugador = True #jugador es verdadero
while True: #mientras sea verdadero
    diseño_tablero(tablero) #llamar la función tablero
    if jugador:
        jugada(tablero) #llamar la función jugada
        time.sleep(1) #esperar un segundo
        victoria = ganador(tablero, "O") #calcular la victoria
    else: 
        print("\nMi turno\n")
        movimiento_computadora(tablero) #llamar la función dibujar movimiento 
        victoria = ganador(tablero, "X") #calcular la victoria 
    if victoria or not campos_libres(tablero): #si hay victoria o no hay campos libres
        break #terminar el juego
    jugador = not jugador #cambiar el jugador 

diseño_tablero(tablero) #llamar la función tablero
if victoria == "tu": #si la victoria es del jugador
    print("\nFelicidades, has ganado!!!")
elif victoria == "yo": #si la victoria es del programa
    print("\nTe gané!!!")
else: #si hay empate
    print("\nBien jugado, es un empate!")
