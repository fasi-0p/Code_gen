public class UnionFind {

    int[] parent;
    int[] rank;

    // Constructor to initialize sets
    public UnionFind(int size) {
        parent = new int[size];
        rank = new int[size];

        // Each node is its own parent initially
        for (int i = 0; i < size; i++) {
            parent[i] = i;
            rank[i] = 0;
        }
    }

    // Find with path compression
    public int find(int x) {
        if (parent[x] != x)
            parent[x] = find(parent[x]);  // Compress the path
        return parent[x];
    }

    // Union by rank
    public void union(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);

        // Merge smaller tree under bigger tree
        if (rootX != rootY) {
            if (rank[rootX] < rank[rootY])
                parent[rootX] = rootY;
            else if (rank[rootX] > rank[rootY])
                parent[rootY] = rootX;
            else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
        }
    }

    public static void main(String[] args) {
        UnionFind uf = new UnionFind(5);  // Nodes 0-4

        uf.union(0, 1);
        uf.union(1, 2);

        System.out.println(uf.find(0) == uf.find(2));  // true
        System.out.println(uf.find(0) == uf.find(4));  // false
    }
}
