def floyd(C):
    n = len(C)
    
    # Initialize A matrix with values from C
    A = [row[:] for row in C]
    
    # Set diagonal elements to 0
    for i in range(n):
        A[i][i] = 0

    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = A[i][k] + A[k][j]

    return A

# Sample test cases
C1 = [
    [0, 5, float('inf'), 10],
    [float('inf'), 0, 3, float('inf')],
    [float('inf'), float('inf'), 0, 1],
    [float('inf'), float('inf'), float('inf'), 0]
]

C2 = [
    [0, 3, 6, 15],
    [float('inf'), 0, -2, float('inf')],
    [float('inf'), float('inf'), 0, 2],
    [1, float('inf'), float('inf'), 0]
]

# Compute shortest paths using Floyd's algorithm
print("Shortest paths for C1:")
result1 = floyd(C1)
for row in result1:
    print(row)

print("\nShortest paths for C2:")
result2 = floyd(C2)
for row in result2:
    print(row)
