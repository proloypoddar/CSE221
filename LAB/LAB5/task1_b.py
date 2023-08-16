def find_by_bfs(N, P):
    graph = [[] for _ in range(N + 1)]
    lst = [0] * (N + 1)
    
    for a, b in P:
        graph[b].append(a)
        lst[a] += 1
    
    zero_nodes = []
    for node in range(1, N + 1):
        if lst[node] == 0:
            zero_nodes.append(node)
    
    order = []
    
    while zero_nodes:
        node = zero_nodes.pop(0)
        order.append(node)
        
        for neighbor in graph[node]:
            lst[neighbor] -= 1
            if lst[neighbor] == 0:
                zero_nodes.append(neighbor)
    
    if len(order) != N:
        return "IMPOSSIBLE"
    
    return order

with open("F:\CSE221\LAB\LAB5\input_task1b.txt", "r") as input_file:
    N, M = map(int, input_file.readline().split())
    P = [tuple(map(int, input_file.readline().split())) for _ in range(M)]

course_order = find_by_bfs(N, P)

with open("F:\CSE221\LAB\LAB5\output_task1b.txt", "w") as output_file:
    if course_order == "IMPOSSIBLE":
        output_file.write(course_order)
    else:
        output_file.write(" ".join(map(str, course_order)))
