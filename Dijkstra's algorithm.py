def dijkstra_algorithm(graph, n):
    S = {1}
    D = [float('inf')] * (n + 1)
    for i in range(2, n + 1):
        D[i] = graph[1][i]
    
    for _ in range(1, n):
        w = -1
        min_distance = float('inf')
        for v in range(1, n + 1):
            if v not in S and D[v] < min_distance:
                min_distance = D[v]
                w = v
        
        S.add(w)
        
        for v in range(1, n + 1):
            if v not in S:
                D[v] = min(D[v], D[w] + graph[w][v])
    
    return D

C = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 4, 0],
    [0, 1, 0, 2, 0],
    [0, 4, 2, 0, 1],
    [0, 0, 0, 1, 0]
]

num_vertices = 4
shortest_distances = dijkstra_algorithm(C, num_vertices)

for i, distance in enumerate(shortest_distances):
print(f"Shortest distance from 1 to {i}: {distance}")

def dijkstra_algorithm(graph, n):
    S = {1}
    D = [float('inf')] * (n + 1)
    for i in range(2, n + 1):
        D[i] = graph[1][i]
    
    for _ in range(1, n):
        w = -1
        min_distance = float('inf')
        for v in range(1, n + 1):
            if v not in S and D[v] < min_distance:
                min_distance = D[v]
                w = v
        
        S.add(w)
        
        for v in range(1, n + 1):
            if v not in S:
                D[v] = min(D[v], D[w] + graph[w][v])
    
    return D

C = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 4, 0],
    [0, 1, 0, 2, 0],
    [0, 4, 2, 0, 1],
    [0, 0, 0, 1, 0]
]

num_vertices = 4
shortest_distances = dijkstra_algorithm(C, num_vertices)

for i, distance in enumerate(shortest_distances):
print(f"Shortest distance from 1 to {i}: {distance}")
