def bfs(graph, start, target):
    queue = [(start, [start])]
    visited = set()
    while queue:
        current, path = queue.pop(0)
        if current == target:
            return len(path) - 1, path
        visited.add(current)
        for i in graph[current]:
            if i not in visited:
                queue.append((i, path + [i]))
    return None
def path_finder():
    with open("F:/CSE221/LAB/LAB4/input_task5.txt", "r") as file:
        N, M, D = map(int, file.readline().split())
        graph = {i: [] for i in range(1, N+1)}
        for _ in range(M):
            u, v = map(int, file.readline().split())
            graph[u].append(v)
            graph[v].append(u)

    min_time, path = bfs(graph, 1, D)

    with open( "F:/CSE221/LAB/LAB4/output_task5.txt", "w") as file2:
        if min_time is None:
            file2.write("Destination city D is not reachable from city 1.")
        else:
            file2.write (f"Time {min_time}\n")
            file2.write("Shortest Path: "+" ".join(map(str, path)))
path_finder()
