#include <iostream>
#include <vector>
using namespace std;

// DFS recursive function
void dfs(int node, const vector<vector<int>>& adj, vector<bool>& visited) {
    visited[node] = true;
    cout << node << " ";

    for (int neighbor : adj[node]) {
        if (!visited[neighbor]) {
            dfs(neighbor, adj, visited);
        }
    }
}

// ✅ Use-case
int main() {
    // Graph: 0-1-2-3-4
    vector<vector<int>> adj = {
        {1},        // 0
        {0, 2, 3},  // 1
        {1, 4},     // 2
        {1},        // 3
        {2}         // 4
    };

    vector<bool> visited(5, false);
    cout << "DFS traversal: ";
    dfs(0, adj, visited);  // Output: DFS traversal: 0 1 2 4 3
}
