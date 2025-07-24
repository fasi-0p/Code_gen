#include <iostream>
#include <vector>
#include <queue>
using namespace std;
typedef pair<int, int> pii;

void dijkstra(int src, const vector<vector<pii>>& adj, int n) {
    vector<int> dist(n, INT_MAX);   // Distance from src
    priority_queue<pii, vector<pii>, greater<pii>> pq;  // Min-heap

    dist[src] = 0;
    pq.push({0, src});

    while (!pq.empty()) {
        int cost = pq.top().first;
        int u = pq.top().second;
        pq.pop();

        for (auto& [v, w] : adj[u]) {
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }

    // Print shortest distances
    cout << "Shortest distances from node " << src << ":\n";
    for (int i = 0; i < n; i++) {
        cout << "To node " << i << ": " << dist[i] << endl;
    }
}

// ✅ Use-case
int main() {
    int n = 5;
    vector<vector<pii>> adj(n);
    // Add edges: u --(w)--> v
    adj[0].push_back({1, 2});
    adj[0].push_back({2, 4});
    adj[1].push_back({2, 1});
    adj[1].push_back({3, 7});
    adj[2].push_back({4, 3});
    adj[3].push_back({4, 1});

    dijkstra(0, adj, n);
}
