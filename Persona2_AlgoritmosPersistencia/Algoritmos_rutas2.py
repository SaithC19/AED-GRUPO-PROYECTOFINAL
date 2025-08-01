def dijkstra(self, inicio):
    distancias = {v: float('inf') for v in self.vertices}
    padres = {v: None for v in self.vertices}
    distancias[inicio] = 0
    cola = [(0, inicio)]

    while cola:
        dist_actual, u = heapq.heappop(cola)
        if dist_actual > distancias[u]:
            continue
        for v, datos in self.vertices[u].items():
            nueva_dist = dist_actual + datos['distancia']
            if nueva_dist < distancias[v]:
                distancias[v] = nueva_dist
                padres[v] = u
                heapq.heappush(cola, (nueva_dist, v))
    return distancias, padres

def obtener_ruta(self, inicio, fin):
    _, padres = self.dijkstra(inicio)
    ruta = []
    actual = fin
    while actual is not None:
        ruta.append(actual)
        actual = padres[actual]
    ruta.reverse()
    return ruta if ruta and ruta[0] == inicio else []

def bfs(self, inicio):
    visitados = set()
    cola = deque([inicio])
    orden = []

    while cola:
        nodo = cola.popleft()
        if nodo not in visitados:
            visitados.add(nodo)
            orden.append(nodo)
            for vecino in self.vertices[nodo]:
                if vecino not in visitados:
                    cola.append(vecino)
    return orden
