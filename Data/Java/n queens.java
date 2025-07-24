public class NQueens {

    // Check if placing a queen at (row, col) is safe
    static boolean isSafe(char[][] board, int row, int col) {
        int n = board.length;

        // Check column
        for (int i = 0; i < row; i++)
            if (board[i][col] == 'Q') return false;

        // Check left diagonal
        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--)
            if (board[i][j] == 'Q') return false;

        // Check right diagonal
        for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++)
            if (board[i][j] == 'Q') return false;

        return true;  // Safe to place queen
    }

    // Backtracking function to solve N-Queens
    static void solve(char[][] board, int row) {
        int n = board.length;

        if (row == n) {  // All queens placed
            for (char[] r : board)
                System.out.println(new String(r));
            System.out.println();
            return;
        }

        for (int col = 0; col < n; col++) {
            if (isSafe(board, row, col)) {
                board[row][col] = 'Q';     // Place queen
                solve(board, row + 1);     // Recurse to next row
                board[row][col] = '.';     // Backtrack
            }
        }
    }

    public static void main(String[] args) {
        int n = 4;
        char[][] board = new char[n][n];
        for (char[] row : board)
            java.util.Arrays.fill(row, '.');

        solve(board, 0);
    }
}
