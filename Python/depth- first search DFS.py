def dfs(graph, start, visited=None, result=None):
    """
    Depth-First Search (DFS):
    - Visits nodes deeply before going wide (LIFO).
    - Can be implemented recursively or using a stack.
    - Time Complexity: O(V + E)
    """
    if visited is None:
        visited = set()
    if result is None:
        result = []

    visited.add(start)       # Mark node as visited
    result.append(start)     # Store node in result

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, result)  # Recur for unvisited neighbors

    return result

# ✅ Example graph and DFS call
print("DFS Traversal:", dfs(graph, 'A'))  # Output: ['A', 'B', 'D', 'E', 'C', 'F']
