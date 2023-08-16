def find_course_order(N, P):
    def dfs(node):
        visited[node] = 1
        for i in graph[node]:
            if visited[i] == 0:
                if not dfs(i):
                    return False
            elif visited[i] == 1:
                return False
        visited[node] = 2
        order.append(node)
        return True
    graph = [[] for _ in range(N + 1)]
    for a, b in P:
        graph[b].append(a)
    
    visited = [0] * (N + 1)
    order = []
    
    for node in range(1, N + 1):
        if visited[node] == 0:
            if not dfs(node):
                return "IMPOSSIBLE"
    return reversed(order)
with open("F:\CSE221\LAB\LAB5\input_task1a.txt", "r") as input_file:
    N, M = map(int, input_file.readline().split())
    P = [tuple(map(int, line.split())) for line in input_file]
course_order = find_course_order(N, P)
with open("F:\CSE221\LAB\LAB5\output_task1a.txt", "w") as output_file:
    if course_order == "IMPOSSIBLE":
        output_file.write(course_order)
    else:
        output_file.write(" ".join(map(str, course_order)))
