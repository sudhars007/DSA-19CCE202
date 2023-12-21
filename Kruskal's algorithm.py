class DisjointSet:
    def __init__(self, vertices):
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)

        if root1 == root2:
            return False

        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

        return True


def kruskal(graph):
    mst = []
    edge_list = [(weight, u, v) for u, neighbors in graph.items() for v, weight in neighbors]
    edge_list.sort()

    disjoint_set = DisjointSet(graph.keys())

    for weight, u, v in edge_list:
        if disjoint_set.union(u, v):
            mst.append((u, v, weight))

    return mst


# Test Case 1
graph1 = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 2)],
    'D': [('B', 1), ('C', 2)]
}

print("Minimum Spanning Tree Edges for Test Case 1:")
print(kruskal(graph1))

# Test Case 2
graph2 = {
    '1': [('2', 3), ('3', 1)],
    '2': [('1', 3), ('3', 1), ('4', 6), ('5', 5)],
    '3': [('1', 1), ('2', 1), ('4', 3)],
    '4': [('2', 6), ('3', 3), ('5', 2)],
    '5': [('2', 5), ('4', 2)]
}

print("\nMinimum Spanning Tree Edges for Test Case 2:")
print(kruskal(graph2))
