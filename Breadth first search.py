from collections import deque

def BFS(graph, start):
    color = {}  # WHITE, GRAY, BLACK
    distance = {}
    predecessor = {}
    
    # Initialize vertices
    for vertex in graph:
        color[vertex] = 'WHITE'
        distance[vertex] = float('inf')
        predecessor[vertex] = None
    
    color[start] = 'GRAY'
    distance[start] = 0
    predecessor[start] = None
    
    queue = deque()
    queue.append(start)
    
    while queue:
        u = queue.popleft()
        
        for v in graph[u]:
            if color[v] == 'WHITE':
                color[v] = 'GRAY'
                distance[v] = distance[u] + 1
                predecessor[v] = u
                queue.append(v)
        
        color[u] = 'BLACK'
    
    return distance, predecessor

# Test Case 1
graph1 = {
    's': ['r', 'w'],
    'r': ['s', 'v'],
    't': ['w', 'x', 'u'],
    'u': ['t', 'x', 'y'],
    'v': ['r'],
    'w': ['s', 't', 'x'],
    'x': ['w', 't', 'u', 'y'],
    'y': ['x', 'u']
}

dist1, pred1 = BFS(graph1, 's')
print("Distance from 's' to each vertex:", dist1)
print("Predecessors:", pred1)

# Test Case 2
graph2 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

dist2, pred2 = BFS(graph2, 'A')
print("\nDistance from 'A' to each vertex:", dist2)
print("Predecessors:", pred2)
