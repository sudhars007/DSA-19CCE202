import heapq

def prim(graph, start):
    # Priority queue to hold edges
    pq = [(0, start)]
    visited = set()
    mst_edges = []
    
    while pq:
        weight, vertex = heapq.heappop(pq)
        if vertex not in visited:
            visited.add(vertex)
            
            for neighbor, edge_weight in graph[vertex]:
                if neighbor not in visited:
                    heapq.heappush(pq, (edge_weight, neighbor))
                    mst_edges.append((vertex, neighbor, edge_weight))
                    
    return mst_edges

# Test Case 1
graph1 = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 2)],
    'D': [('B', 1), ('C', 2)]
}

print("Minimum Spanning Tree Edges for Test Case 1:")
print(prim(graph1, 'A'))

# Test Case 2
graph2 = {
    '1': [('2', 3), ('3', 1)],
    '2': [('1', 3), ('3', 1), ('4', 6), ('5', 5)],
    '3': [('1', 1), ('2', 1), ('4', 3)],
    '4': [('2', 6), ('3', 3), ('5', 2)],
    '5': [('2', 5), ('4', 2)]
}

print("\nMinimum Spanning Tree Edges for Test Case 2:")
print(prim(graph2, '1')))
