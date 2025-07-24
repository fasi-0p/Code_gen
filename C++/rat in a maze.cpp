#include <iostream>
#include <vector>
using namespace std;

void solveMaze(int x, int y, vector<vector<int>>& maze, vector<vector<int>>& visited,
               string path, vector<string>& paths, int n) {
    // Boundary + visited + wall check
    if (x < 0 || y < 0 || x >= n || y >= n || maze[x][y] == 0 || visited[x][y]) return;

    // Reached destination
    if (x == n - 1 && y == n - 1) {
        paths.push_back(path);
        return;
    }

    visited[x][y] = 1;

    // Move Down
    solveMaze(x + 1, y, maze, visited, path + 'D', paths, n);
    // Move Left
    solveMaze(x, y - 1, maze, visited, path + 'L', paths, n);
    // Move Right
    solveMaze(x, y + 1, maze, visited, path + 'R', paths, n);
    // Move Up
    solveMaze(x - 1, y, maze, visited, path + 'U', paths, n);

    visited[x][y] = 0;  // Backtrack
}

// ✅ Use-case
int main() {
    vector<vector<int>> maze = {
        {1, 0, 0, 0},
        {1, 1, 0, 1},
        {0, 1, 0, 0},
        {1, 1, 1, 1}
    };
    int n = 4;
    vector<vector<int>> visited(n, vector<int>(n, 0));
    vector<string> paths;

    if (maze[0][0] == 1)
        solveMaze(0, 0, maze, visited, "", paths, n);

    for (string& path : paths)
        cout << path << endl;  // All valid paths
}
