import heapq

def dijkstra(graph, start):
    # Inicializa las distancias a infinito para todos los nodos excepto el nodo de inicio.
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Crear una cola de prioridad para almacenar nodos no visitados.
    priority_queue = [(0, start)]

    while priority_queue:
        # Obtiene el nodo con la distancia más corta.
        current_distance, current_node = heapq.heappop(priority_queue)

        # Si la distancia actual es mayor que la almacenada, omítelo.
        if current_distance > distances[current_node]:
            continue

        # Explora los vecinos del nodo actual.
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Si encontramos una distancia más corta hacia el vecino, actualiza la distancia.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Ejemplo de uso
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
start_node = 'A'

result = dijkstra(graph, start_node)
print("Nodo de inicio: ",start_node,"\n",result)

