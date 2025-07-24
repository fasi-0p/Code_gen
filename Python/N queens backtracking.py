def solve_n_queens(n):
    """
    N-Queens Problem:
    - Place n queens on an n×n board so that no two queens attack each other.
    - Backtracking: try placing queens row by row, and backtrack if unsafe.
    - Time Complexity: O(N!), exponential due to backtracking.
    """
    result = []
    board = [["."] * n for _ in range(n)]  # Initialize board with "."

    def is_safe(row, col):
        # Check vertical ↑
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        # Check upper-left ↖ diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        # Check upper-right ↗ diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True

    def backtrack(row):
        if row == n:
            # If all rows filled, store result
            result.append(["".join(r) for r in board])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 'Q'       # Place queen
                backtrack(row + 1)          # Recurse to next row
                board[row][col] = '.'       # Backtrack

    backtrack(0)
    return result

# ✅ Example
solutions = solve_n_queens(4)
for s in solutions:
    print("\n".join(s))
    print("---")
