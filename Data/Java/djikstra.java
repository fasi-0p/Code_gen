import java.util.*;

public class Dijkstra {

    // Function to perform Dijkstra's algorithm
    public static Map<Integer, Integer> dijkstra(Map<Integer, List<int[]>> graph, int start) {
        Map<Integer, Integer> dist = new HashMap<>();           // Node → Distance from start
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));

        // Initialize distances to infinity
        for (int node : graph.keySet())
            dist.put(node, Integer.MAX_VALUE);

        dist.put(start, 0);                      // Distance to source is 0
        pq.add(new int[]{start, 0});             // Add source to queue

        while (!pq.isEmpty()) {
            int[] current = pq.poll();           // Node with minimum distance
            int node = current[0];
            int cost = current[1];

            // Visit all neighbors
            for (int[] neighbor : graph.get(node)) {
                int nextNode = neighbor[0];
                int weight = neighbor[1];
                int newDist = cost + weight;

                // Relaxation: update distance if shorter path is found
                if (newDist < dist.get(nextNode)) {
                    dist.put(nextNode, newDist);
                    pq.add(new int[]{nextNode, newDist});
                }
            }
        }

        return dist;
    }

    public static void main(String[] args) {
        // Graph: node → list of [neighbor, weight]
        Map<Integer, List<int[]>> graph = new HashMap<>();
        graph.put(0, Arrays.asList(new int[]{1, 4}, new int[]{2, 1}));
        graph.put(1, Arrays.asList(new int[]{3, 1}));
        graph.put(2, Arrays.asList(new int[]{1, 2}, new int[]{3, 5}));
        graph.put(3, new ArrayList<>());

        Map<Integer, Integer> result = dijkstra(graph, 0);

        System.out.println("Shortest distances from node 0:");
        for (int node : result.keySet())
            System.out.println("To node " + node + " → " + result.get(node));

        // Expected: 0→0, 1→3, 2→1, 3→4
    }
}
