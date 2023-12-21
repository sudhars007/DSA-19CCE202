def compute_optimal_costs(C, z):
    J = {z: 0}
    while len(J) < len(C):
        for i in range(len(C)):
            if i not in J:
                if all(j in J for j in range(len(C)) if C[i][j] is not None):
                    J[i] = min(C[i][j] + J[j] for j in range(len(C)) if C[i][j] is not None)
    return J

C = [
    [None, None, 2, 1],
    [None, None, None, None],
    [None, None, None, None],
    [None, 4, None, None]
]

destination = 1
optimal_costs = compute_optimal_costs(C, destination)

for vertex, cost in optimal_costs.items():
    print(f"J({vertex}) = {cost}")
