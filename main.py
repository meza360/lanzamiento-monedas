# Giovani David Meza Poggio - 9941-18-14676
# Estadistica 1
# Lanzamiento de monedas
import os
import random
print("Bienvenido al lanzamiento de monedas")
print("1. Empezar")
print("2. Salir")
# 1 cara
# 2 escudo
j1Points = 100
j2Points = 100

def validaGanador(p1, p2):
    if p1 == 1 and p2 == 2:
        print("Gana J2 Pierde J1")
        return 2
    elif p1 == 2 and p2 == 1:
        print("Gana J2 Pierde J1")
        return 2
    elif p1 == 1 and p2 == 1:
        print("Gana J1 Pierde J2")
        return 1
    elif p1 == 2 and p2 == 2:
        print("Gana J1 Pierde J2")
        return 1

def validaPuntos(lanzamientoGanador):
    global j1Points
    global j2Points
    if lanzamientoGanador == 1:
        j1Points += 10
        j2Points -= 10
    else:
        j2Points += 10
        j1Points -= 10
    if j1Points <= 50:
        print("Jugador 1 ha perdido")
        os.abort()
    if j2Points <= 50:
        print("Jugador 2 ha perdido")
        os.abort()

def lanzaDados():
    return random.randint(1, 2)

def retornaMoneda(valor):
    if valor == 1:
        return "Cara"
    else:
        return "Escudo"
        
while True:
    print("Condiciones de juego")
    print("----------Judador 2-")
    print("---------|----|----|")
    print("---------| C  | E  |")
    print("Jugador C|G1P2|G2P1|")
    print("---1--- E|G2P1|G1P2|")
    print("---------|----|----|")
    print("El juego termina cuando alguno de los dos jugadores llega a 50 puntos")
    print("Lanzando monedas...")
    j1 = lanzaDados()
    j2 = lanzaDados()
    print("Jugador 1: ", retornaMoneda(j1))
    print("Jugador 2: ", retornaMoneda(j2))
    validaPuntos(validaGanador(j1, j2))
    print("Puntos Jugador 1: ", j1Points)
    print("Puntos Jugador 2: ", j2Points)
    print("Presione Enter para siguiente lanzamiento")
    input()