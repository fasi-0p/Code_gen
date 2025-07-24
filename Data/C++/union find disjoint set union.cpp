#include <iostream>
#include <vector>
using namespace std;

class UnionFind {
private:
    vector<int> parent, rank;

public:
    UnionFind(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        // Initialize each node as its own parent
        for (int i = 0; i < n; i++) parent[i] = i;
    }

    // Find the root of a node with path compression
    int find(int x) {
        if (x != parent[x])
            parent[x] = find(parent[x]);  // Path compression
        return parent[x];
    }

    // Union two sets by rank
    void unite(int x, int y) {
        int rootX = find(x), rootY = find(y);
        if (rootX == rootY) return;

        if (rank[rootX] < rank[rootY])
            parent[rootX] = rootY;
        else if (rank[rootX] > rank[rootY])
            parent[rootY] = rootX;
        else {
            parent[rootY] = rootX;
            rank[rootX]++;
        }
    }

    // Check if two elements are in same set
    bool connected(int x, int y) {
        return find(x) == find(y);
    }
};

// ✅ Use-case
int main() {
    UnionFind uf(5);  // Nodes: 0,1,2,3,4

    uf.unite(0, 1);
    uf.unite(1, 2);
    uf.unite(3, 4);

    cout << "Are 0 and 2 connected? " << (uf.connected(0, 2) ? "Yes" : "No") << endl;  // Yes
    cout << "Are 0 and 4 connected? " << (uf.connected(0, 4) ? "Yes" : "No") << endl;  // No
}
