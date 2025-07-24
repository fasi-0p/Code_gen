def rat_in_maze(maze):
    """
    Rat in a Maze:
    - Find all paths from (0, 0) to (n-1, n-1) only moving Down, Left, Right, Up.
    - Only move through 1s (open path), avoid 0s (walls).
    - Uses backtracking to explore all directions.
    """
    n = len(maze)
    result = []
    directions = [('D', 1, 0), ('L', 0, -1), ('R', 0, 1), ('U', -1, 0)]
    visited = [[False]*n for _ in range(n)]

    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < n and maze[x][y] == 1 and not visited[x][y]

    def backtrack(x, y, path):
        if x == n-1 and y == n-1:
            result.append(path)
            return
        for dir_symbol, dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                visited[x][y] = True
                backtrack(nx, ny, path + dir_symbol)
                visited[x][y] = False  # Backtrack

    if maze[0][0] == 1:
        backtrack(0, 0, "")

    return result

# ✅ Example Maze
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]
print("Maze Paths:", rat_in_maze(maze))
