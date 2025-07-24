class DisjointSet:
    """
    Union-Find (Disjoint Set):
    - Supports union and find operations.
    - Used in Kruskal’s algorithm, detecting cycles.
    - Optimized with path compression and union by rank.
    - Time Complexity: nearly O(1) per operation (amortized)
    """
    def __init__(self, n):
        self.parent = [i for i in range(n)]  # Initially each node is its own parent
        self.rank = [0] * n  # Rank for optimization

    def find(self, x):
        # Path compression: set parent[x] to root directly
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Find roots of both sets
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return  # Already in the same set

        # Union by rank: attach smaller tree under larger
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

# ✅ Example usage
ds = DisjointSet(5)
ds.union(0, 1)
ds.union(1, 2)
print("Find(0):", ds.find(0))  # Output: 0 or root node
print("Find(2):", ds.find(2))  # Output: same as Find(0)
print("Find(3):", ds.find(3))  # Output: 3 (separate set)
