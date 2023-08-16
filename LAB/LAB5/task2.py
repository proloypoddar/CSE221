def Courses_number(N, P):
    graph = [[] for i in range(N + 1)]
    lst = [0] * (N + 1)
    
    for a, b in P:
        graph[a].append(b)
        lst[b] += 1
    
    value = []
    for node in range(1, N + 1):
        if lst[node] == 0:
            value.append(node)
    
    result = []
    
    while value:
        node = value.pop(0)
        result.append(node)
        
        for i in graph[node]:
            lst[i] -= 1
            if lst[i] == 0:
                value.append(i)
    
    if len(result) != N:
        return "IMPOSSIBLE"
    
    return (" ".join(map(str, result)))

with open("F:\CSE221\LAB\LAB5\input_task2.txt", "r") as input_file:
    N, M = map(int, input_file.readline().split())
    P = [tuple(map(int, line.split())) for line in input_file]

x = Courses_number(N, P)

with open("F:\CSE221\LAB\LAB5\output_task2.txt", "w") as output_file:
    output_file.write(x)
