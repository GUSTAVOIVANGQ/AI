# 4_puzzle.py
from typing import List, Tuple
from estructuras_datos import Cola

class Puzzle4:
    def __init__(self, estado: List[List[int]]):
        self.estado = estado

    def __eq__(self, other):
        return self.estado == other.estado

    def __hash__(self):
        return hash(str(self.estado))

    def obtener_movimientos_posibles(self) -> List[str]:
        movimientos = []
        fila_vacia, col_vacia = None, None
        
        for i in range(2):
            for j in range(2):
                if self.estado[i][j] == 0:
                    fila_vacia, col_vacia = i, j
                    break
            if fila_vacia is not None:
                break

        if fila_vacia > 0:
            movimientos.append('arriba')
        if fila_vacia < 1:
            movimientos.append('abajo')
        if col_vacia > 0:
            movimientos.append('izquierda')
        if col_vacia < 1:
            movimientos.append('derecha')

        return movimientos

    def aplicar_movimiento(self, movimiento: str) -> 'Puzzle4':
        nuevo_estado = [fila[:] for fila in self.estado]
        fila_vacia, col_vacia = None, None
        
        for i in range(2):
            for j in range(2):
                if nuevo_estado[i][j] == 0:
                    fila_vacia, col_vacia = i, j
                    break
            if fila_vacia is not None:
                break

        if movimiento == 'arriba':
            nuevo_estado[fila_vacia][col_vacia], nuevo_estado[fila_vacia - 1][col_vacia] = \
                nuevo_estado[fila_vacia - 1][col_vacia], nuevo_estado[fila_vacia][col_vacia]
        elif movimiento == 'abajo':
            nuevo_estado[fila_vacia][col_vacia], nuevo_estado[fila_vacia + 1][col_vacia] = \
                nuevo_estado[fila_vacia + 1][col_vacia], nuevo_estado[fila_vacia][col_vacia]
        elif movimiento == 'izquierda':
            nuevo_estado[fila_vacia][col_vacia], nuevo_estado[fila_vacia][col_vacia - 1] = \
                nuevo_estado[fila_vacia][col_vacia - 1], nuevo_estado[fila_vacia][col_vacia]
        elif movimiento == 'derecha':
            nuevo_estado[fila_vacia][col_vacia], nuevo_estado[fila_vacia][col_vacia + 1] = \
                nuevo_estado[fila_vacia][col_vacia + 1], nuevo_estado[fila_vacia][col_vacia]

        return Puzzle4(nuevo_estado)

    def imprimir_4puzzle(self):
        for fila in self.estado:
            print(fila)
        print()

def resolver_4puzzle(estado_inicial: Puzzle4, estado_objetivo: Puzzle4) -> List[str]:
    cola = Cola()
    visitados = set()

    cola.insertar((estado_inicial, []))

    while not cola.esta_vacia():
        estado_actual, camino = cola.quitar()

        if estado_actual == estado_objetivo:
            return camino

        if estado_actual not in visitados:
            visitados.add(estado_actual)

            for movimiento in estado_actual.obtener_movimientos_posibles():
                nuevo_estado = estado_actual.aplicar_movimiento(movimiento)
                if nuevo_estado not in visitados:
                    nuevo_camino = camino + [movimiento]
                    cola.insertar((nuevo_estado, nuevo_camino))
                    print(f"Movimiento: {movimiento}")
                    nuevo_estado.imprimir_4puzzle()

    return None

# Programa principal
estado_inicial = Puzzle4([
    [1, 2], 
    [0, 3]])  # 0 representa el espacio vacío
estado_objetivo = Puzzle4([
    [1, 2], 
    [3, 0]])

solucion = resolver_4puzzle(estado_inicial, estado_objetivo)

if solucion:
    print(f"Solución encontrada en {len(solucion)} movimientos:")
    print(solucion)
else:
    print("No se pudo resolver el puzzle")

# Imprimir el estado inicial y final del puzzle
print("Estado inicial:")
estado_inicial.imprimir_4puzzle()

print("Estado objetivo:")
estado_objetivo.imprimir_4puzzle()