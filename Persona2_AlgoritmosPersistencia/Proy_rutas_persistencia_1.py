import heapq
from collections import deque

#cargar el grafo desde archivo rutas.txt
def cargar_grafo_desde_archivo(nombre_archivo):
    grafo = {}
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue
            if ":" in linea:
                nodo, conexiones_str = [x.strip() for x in linea.split(":", 1)]
            else:
                nodo = linea.strip()
                conexiones_str = ""
            if nodo not in grafo:
                grafo[nodo] = {}
            if conexiones_str:
                conexiones = conexiones_str.split(";")
                for conexion in conexiones:
                    if not conexion.strip():
                        continue
                    vecino, distancia = [x.strip() for x in conexion.split(",")]
                    grafo[nodo][vecino] = float(distancia)
                    if vecino not in grafo:
                        grafo[vecino] = {}
    return grafo

#guardar grafo en archivo rutas.txt
def guardar_grafo_en_archivo(nombre_archivo, grafo):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        for nodo, vecinos in grafo.items():
            conexiones = []
            for vecino, distancia in vecinos.items():
                conexiones.append(f"{vecino},{distancia}")
            linea = nodo + ":" + ";".join(conexiones) + "\n"
            archivo.write(linea)

#algoritmo de Dijkstra para ruta óptima
def dijkstra(grafo, inicio, destino=None):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    padres = {nodo: None for nodo in grafo}
    cola = [(0, inicio)]
    visitados = set()

    while cola:
        dist_actual, nodo_actual = heapq.heappop(cola)
        if nodo_actual in visitados:
            continue
        visitados.add(nodo_actual)

        if nodo_actual == destino:
            break

        for vecino, peso in grafo[nodo_actual].items():
            nueva_distancia = dist_actual + peso
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                padres[vecino] = nodo_actual
                heapq.heappush(cola, (nueva_distancia, vecino))

    def reconstruir_camino(hasta):
        camino = []
        actual = hasta
        while actual is not None:
            camino.append(actual)
            actual = padres[actual]
        return camino[::-1]

    if destino:
        if distancias[destino] == float('inf'):
            return None, float('inf')
        return reconstruir_camino(destino), distancias[destino]
    else:
        rutas = {}
        for nodo in grafo:
            if distancias[nodo] != float('inf'):
                rutas[nodo] = {
                    'camino': reconstruir_camino(nodo),
                    'distancia': distancias[nodo]
                }
        return rutas

#BFS para exploración por niveles
def bfs(grafo, inicio):
    visitados = set()
    cola = deque([inicio])
    orden = []

    while cola:
        nodo = cola.popleft()
        if nodo not in visitados:
            visitados.add(nodo)
            orden.append(nodo)
            for vecino in grafo[nodo]:
                if vecino not in visitados:
                    cola.append(vecino)
    return orden

#DFS para exploración profunda
def dfs(grafo, inicio):
    visitados = set()
    pila = [inicio]
    orden = []

    while pila:
        nodo = pila.pop()
        if nodo not in visitados:
            visitados.add(nodo)
            orden.append(nodo)
            for vecino in grafo[nodo]:
                if vecino not in visitados:
                    pila.append(vecino)
    return orden

def main():
    grafo = cargar_grafo_desde_archivo("rutas.txt")
    print("Grafo cargado:")
    for nodo, vecinos in grafo.items():
        print(f"{nodo}: {vecinos}")

    inicio = "El Ejido"
    destino = "Quicentro Shopping"
    ruta, distancia = dijkstra(grafo, inicio, destino)

    print(f"\nRuta más corta de '{inicio}' a '{destino}':")
    if ruta:
        print(" -> ".join(ruta))
        print(f"Distancia total: {distancia} km")
    else:
        print("No existe ruta")

if __name__ == "__main__":
    main()
    