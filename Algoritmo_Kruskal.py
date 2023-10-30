class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y

def kruskal(graph, find_minimum=True):
    edges = []

    for node in graph:
        for neighbor, weight in graph[node]:
            edges.append((node, neighbor, weight))

    edges.sort(key=lambda x: x[2], reverse=not find_minimum)

    num_nodes = len(graph)
    mst_edges = []
    union_find = UnionFind(num_nodes)

    for edge in edges:
        node_a, node_b, weight = edge
        if union_find.find(node_a) != union_find.find(node_b):
            union_find.union(node_a, node_b)
            mst_edges.append(edge)
            print(f"Added edge: ({node_a} - {node_b}) with weight {weight}")

    return mst_edges

# Ejemplo de uso
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 4), ('D', 5)],
    'C': [('A', 3), ('B', 4), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

print("\nMinimum Spanning Tree:")
minimum_spanning_tree = kruskal(graph, find_minimum=True)
print("\nMaximum Spanning Tree:")
maximum_spanning_tree = kruskal(graph, find_minimum=False)
