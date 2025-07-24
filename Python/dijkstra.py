import heapq

def dijkstra(graph, start):
    """
    Dijkstra's Algorithm:
    - Finds shortest path from start to all other nodes.
    - Uses a priority queue (min-heap) to get closest unvisited node.
    - Time Complexity: O((V + E) log V)
    """
    distances = {node: float('inf') for node in graph}  # Initialize distances
    distances[start] = 0  # Distance to start is 0

    min_heap = [(0, start)]  # Heap of (distance, node)

    while min_heap:
        current_dist, current_node = heapq.heappop(min_heap)

        # If current distance is already worse, skip
        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight  # Total distance to neighbor
            if distance < distances[neighbor]:
                distances[neighbor] = distance  # Update shortest distance
                heapq.heappush(min_heap, (distance, neighbor))

    return distances

# ✅ Example weighted graph
weighted_graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}
print("Dijkstra Distances:", dijkstra(weighted_graph, 'A'))
# Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
