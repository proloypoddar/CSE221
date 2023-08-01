def dfs(graph, start_node):
    visited = set()
    stack = [start_node]
    visited.add(start_node)

    with open("F:\CSE221\LAB\LAB4\output_task3.txt", "w") as file:
        while stack:
            current_node = stack.pop()
            file.write(str(current_node) + ' ')

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)

dict = {}
with open("F:\CSE221\LAB\LAB4\input_task3.txt", "r") as file:
    lines = file.readlines()[1:]
    data = [list(map(int, i.split())) for i in lines]

for i in data:
    a, b = i
    if a not in dict:
        dict[a] = []
    if b not in dict:
        dict[b] = []
    dict[a].append(b)
    dict[b].append(a)
dfs(dict, 1)
