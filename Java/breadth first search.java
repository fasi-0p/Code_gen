import java.util.*;

public class BFS {

    // Function to perform BFS from a given start node
    public static void bfs(int start, Map<Integer, List<Integer>> graph) {
        Queue<Integer> queue = new LinkedList<>();         // Queue to store nodes to visit
        Set<Integer> visited = new HashSet<>();            // Set to keep track of visited nodes

        queue.add(start);      // Enqueue starting node
        visited.add(start);    // Mark it as visited

        System.out.print("BFS Traversal: ");

        while (!queue.isEmpty()) {
            int current = queue.poll();                    // Dequeue current node
            System.out.print(current + " ");

            // Visit all unvisited neighbors
            for (int neighbor : graph.get(current)) {
                if (!visited.contains(neighbor)) {
                    queue.add(neighbor);                   // Enqueue neighbor
                    visited.add(neighbor);                 // Mark as visited
                }
            }
        }
        System.out.println();
    }

    public static void main(String[] args) {
        // Sample graph as adjacency list
        Map<Integer, List<Integer>> graph = new HashMap<>();
        graph.put(0, Arrays.asList(1, 2));
        graph.put(1, Arrays.asList(0, 3, 4));
        graph.put(2, Arrays.asList(0, 5));
        graph.put(3, Arrays.asList(1));
        graph.put(4, Arrays.asList(1));
        graph.put(5, Arrays.asList(2));

        bfs(0, graph);  // Output: 0 1 2 3 4 5
    }
}
