import heapq
import time
from estructuras_datos import Pila, Cola, ListaGenerica, Nodo


def heuristica(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def get_vecinos(maze, nodo):
    vecinos = []
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = nodo.posicion[0] + dx, nodo.posicion[1] + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
            vecinos.append((nx, ny))
    return vecinos

def a_star(maze, start, end):
    cola_prioridad = []
    heapq.heappush(cola_prioridad, Nodo(start, h=heuristica(start, end)))
    visitados = set()

    while cola_prioridad:
        nodo_actual = heapq.heappop(cola_prioridad)

        if nodo_actual.posicion == end:
            camino = []
            while nodo_actual:
                camino.append(nodo_actual.posicion)
                nodo_actual = nodo_actual.padre
            return camino[::-1]

        if nodo_actual.posicion in visitados:
            continue

        visitados.add(nodo_actual.posicion)

        for vecino in get_vecinos(maze, nodo_actual):
            if vecino not in visitados:
                nuevo_g = nodo_actual.g + 1
                nuevo_nodo = Nodo(vecino, g=nuevo_g, h=heuristica(vecino, end), padre=nodo_actual)
                heapq.heappush(cola_prioridad, nuevo_nodo)
                print('-------------------------------------------')
                print_maze(maze, [nodo.posicion for nodo in cola_prioridad])


    return None

def resolver_laberinto(maze, start, end):
    inicio = time.time()
    camino = a_star(maze, start, end)
    fin = time.time()
    tiempo_ejecucion = fin - inicio

    if camino:
        print(f"Camino encontrado: {camino}")
        print(f"Tiempo de ejecución: {tiempo_ejecucion:.6f} segundos")
        return camino
    else:
        print("No se encontró un camino.")


def print_maze(maze, path):
    # print_maze 
    # si es nodo explorado se imprime un punto (.)
    # si es nodo del camino se imprime una X
    # si es nodo de inicio se imprime una I
    # si es nodo de fin se imprime una F
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if (i, j) == start:
                print("I", end=" ")
            elif (i, j) == end:
                print("F", end=" ")
            elif (i, j) in path:
                print("X", end=" ")
            elif maze[i][j] == 1:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()

# Laberinto original
maze = [
    [1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1]
]
start = (0, 1)
end = (3, 4)

print("Resolviendo laberinto original:")
path = resolver_laberinto(maze, start, end)
print_maze(maze, path)

# Laberinto más complejo y de mayor tamaño
maze_complejo = [
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1]
]
start_complejo = (1, 1)
end_complejo = (8, 1)

print("\nResolviendo laberinto más complejo:")
path_complejo = resolver_laberinto(maze_complejo, start_complejo, end_complejo)
print_maze(maze_complejo, path_complejo)