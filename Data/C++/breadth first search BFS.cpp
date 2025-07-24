#include <iostream>
#include <vector>
#include <queue>
using namespace std;

// Perform BFS from starting node
void bfs(int start, const vector<vector<int>>& adj) {
    int n = adj.size();
    vector<bool> visited(n, false);
    queue<int> q;

    visited[start] = true;
    q.push(start);

    cout << "BFS traversal: ";
    while (!q.empty()) {
        int node = q.front();
        q.pop();
        cout << node << " ";

        for (int neighbor : adj[node]) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                q.push(neighbor);
            }
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
    bfs(0, adj);  // Output: BFS traversal: 0 1 2 3 4
}
