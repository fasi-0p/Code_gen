#include <iostream>
#include <vector>
using namespace std;

bool isSafe(vector<string>& board, int row, int col, int n) {
    // Check column above
    for (int i = 0; i < row; i++)
        if (board[i][col] == 'Q') return false;

    // Check left diagonal
    for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--)
        if (board[i][j] == 'Q') return false;

    // Check right diagonal
    for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++)
        if (board[i][j] == 'Q') return false;

    return true;
}

void solve(int row, int n, vector<string>& board, vector<vector<string>>& solutions) {
    if (row == n) {
        solutions.push_back(board);  // Found valid arrangement
        return;
    }

    for (int col = 0; col < n; col++) {
        if (isSafe(board, row, col, n)) {
            board[row][col] = 'Q';            // Place queen
            solve(row + 1, n, board, solutions); // Recur
            board[row][col] = '.';            // Backtrack
        }
    }
}

void nQueens(int n) {
    vector<vector<string>> solutions;
    vector<string> board(n, string(n, '.'));

    solve(0, n, board, solutions);

    // Print solutions
    for (auto& sol : solutions) {
        for (auto& row : sol)
            cout << row << endl;
        cout << endl;
    }
}

// ✅ Use-case
int main() {
    nQueens(4);  // Classic 4x4 N-Queens problem
}
