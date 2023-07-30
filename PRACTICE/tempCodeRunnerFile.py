def find_cycle(graph):
    def dfs(node, parent):
        stack.append(node)
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                cycle.extend(stack[stack.index(neighbor):])
                return True

        stack.pop()
        return False

    stack = []
    cycle = []
    visited = set()

    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return cycle

    return None


graph = {
    "A": ["C", "B"],
    "B": ["D"],
    "C": [],
    "D": ["A", "E"],
    "E": []
}
cycle = find_cycle(graph)
if cycle:
    print("Cycle found:", cycle)
else:
    print("No cycle found.")
