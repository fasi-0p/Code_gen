from collections import deque

def bfs(graph, start):
    """
    Breadth-First Search (BFS):
    - Visits all neighbors level by level (FIFO).
    - Uses a queue to explore nodes in breadth-first manner.
    - Time Complexity: O(V + E), where V = vertices, E = edges.
    """
    visited = set()  # To keep track of visited nodes
    queue = deque([start])  # Initialize queue with starting node
    result = []  # Store traversal order

    while queue:
        node = queue.popleft()  # Pop from front of queue
        if node not in visited:
            visited.add(node)  # Mark node as visited
            result.append(node)  # Add node to result
            for neighbor in graph.get(node, []):
                queue.append(neighbor)  # Add unvisited neighbors to queue

    return result

# ✅ Example graph and BFS call
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': [], 'F': []
}
print("BFS Traversal:", bfs(graph, 'A'))  # Output: ['A', 'B', 'C', 'D', 'E', 'F']
