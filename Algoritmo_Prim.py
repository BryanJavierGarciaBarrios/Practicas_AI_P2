from collections import defaultdict

def prim(graph):
    mst = defaultdict(list)  # Árbol Parcial Mínimo
    visited = set()  # Nodos visitados
    start_node = list(graph.keys())[0]  # Comenzar desde cualquier nodo

    visited.add(start_node)
    num_nodes = len(graph)  # Número total de nodos en el grafo

    while len(visited) < num_nodes:
        edge_candidates = []

        for node in visited:
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    edge_candidates.append((node, neighbor, weight))

        edge_candidates.sort(key=lambda x: x[2])  # Ordenar candidatos por peso
        min_edge = edge_candidates[0]  # Tomar la arista de peso mínimo

        source, dest, weight = min_edge
        visited.add(dest)
        mst[source].append((dest, weight))
        mst[dest].append((source, weight))

        print(f"Added edge: ({source} - {dest}) with weight {weight}")

    return mst

# Ejemplo de uso
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 4), ('D', 5)],
    'C': [('A', 3), ('B', 4), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

minimum_spanning_tree = prim(graph)

print("\nMinimum Spanning Tree:")
for node, edges in minimum_spanning_tree.items():
    for edge in edges:
        print(f"({node} - {edge[0]}) with weight {edge[1]}")

