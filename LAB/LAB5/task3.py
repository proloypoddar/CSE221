def dfs1(node, graph, visited, stack):
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            dfs1(i, graph, visited, stack)
    stack.append(node)
def dfs2(node, reverse_graph, visited, lst):
    visited[node] = True
    lst.append(node)
    for i in reverse_graph[node]:
        if not visited[i]:
            dfs2(i, reverse_graph, visited, lst)
def connection_cheak(n, edges):
    graph = [[] for i in range(n + 1)]
    reverse_graph = [[] for i in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        reverse_graph[v].append(u)
    visited = [False] * (n + 1)
    stack = []
    for i in range(1, n + 1):
        if not visited[i]:
            dfs1(i, graph, visited, stack)
    visited = [0] * (n + 1)
    value = []

    while stack:
        node = stack.pop()
        if not visited[node]:
            lst = []
            dfs2(node, reverse_graph, visited, lst)

            value.append(lst)
    return value
input_file_path = "F:\\CSE221\\LAB\\LAB5\\input_task3.txt"
output_file_path = "F:\\CSE221\\LAB\\LAB5\\output_task3.txt"
with open(input_file_path, 'r') as input_file:
    N, M = map(int, input_file.readline().split())
    edges = [tuple(map(int, line.split())) for line in input_file]
value = connection_cheak(N, edges)
with open(output_file_path, 'w') as output_file:
    for i in value:
        output_file.write(" ".join(map(str, i)) + "\n")


