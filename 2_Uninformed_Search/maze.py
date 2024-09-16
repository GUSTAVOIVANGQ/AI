from typing import List, Tuple
from estructuras_datos import Pila

def resolver_laberinto(laberinto: List[List[int]], inicio: Tuple[int, int], fin: Tuple[int, int]) -> List[Tuple[int, int]]:
    pila = Pila()
    visitados = set()
    
    pila.push((inicio, [inicio]))  # (posición actual, camino)
    
    while not pila.esta_vacia():
        posicion_actual, camino = pila.pop()
        
        if posicion_actual == fin:
            print("---------------------------------")
            imprimir_laberinto(laberinto, camino)
            return camino
        
        if posicion_actual not in visitados:
            visitados.add(posicion_actual)
            
            for movimiento in [(0, 1), (0, -1), (1, 0), (-1, 0)]:  # derecha, izquierda, abajo, arriba
                nueva_posicion = aplicar_movimiento(posicion_actual, movimiento)
                if es_movimiento_valido(laberinto, nueva_posicion) and nueva_posicion not in visitados:
                    nuevo_camino = camino + [nueva_posicion]
                    pila.push((nueva_posicion, nuevo_camino))
        print("---------------------------------")
        imprimir_laberinto(laberinto, camino)
    
    return None  # No se encontró camino

def aplicar_movimiento(posicion: Tuple[int, int], movimiento: Tuple[int, int]) -> Tuple[int, int]:
    return (posicion[0] + movimiento[0], posicion[1] + movimiento[1])

def es_movimiento_valido(laberinto: List[List[int]], posicion: Tuple[int, int]) -> bool:
    filas = len(laberinto)
    columnas = len(laberinto[0])
    fila, columna = posicion
    
    if 0 <= fila < filas and 0 <= columna < columnas and laberinto[fila][columna] == 0:
        return True
    else:
        return False

def imprimir_laberinto(laberinto: List[List[int]], camino: List[Tuple[int, int]]):
    for i, fila in enumerate(laberinto):
        for j, celda in enumerate(fila):
            if (i, j) in camino:
                print("O", end=" ")
            elif celda == 1:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()

# Programa principal
laberinto = [
    [1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1]
]
inicio = (0, 1)
fin = (3, 4)

solucion = resolver_laberinto(laberinto, inicio, fin)
if solucion:
    print("Camino encontrado:")
    print(solucion)
    print("\nVisualización del laberinto:")
    imprimir_laberinto(laberinto, solucion)
else:
    print("No se encontró solución")