public class RatInMaze {

    static void solveMaze(int[][] maze, int row, int col, String path, int n) {
        // If out of bounds or on a blocked cell
        if (row >= n || col >= n || maze[row][col] == 0)
            return;

        // If reached destination
        if (row == n - 1 && col == n - 1) {
            System.out.println(path);
            return;
        }

        // Move Right
        solveMaze(maze, row, col + 1, path + "R", n);

        // Move Down
        solveMaze(maze, row + 1, col, path + "D", n);
    }

    public static void main(String[] args) {
        int[][] maze = {
            {1, 0, 0},
            {1, 1, 0},
            {0, 1, 1}
        };

        int n = maze.length;
        System.out.println("Possible Paths:");
        solveMaze(maze, 0, 0, "", n);  // Output should be: RRDD, RDRD etc depending on maze config
    }
}
