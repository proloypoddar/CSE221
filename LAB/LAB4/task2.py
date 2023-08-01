def bfs(dict, start_node):
    v = set()
    queue = [start_node]
    v.add(start_node)

    with open("F:\CSE221\LAB\LAB4\output_task2.txt", "w") as file:
        while queue:
            curr = queue.pop(0)
            file.write(str(curr) + ' ')

            for i in dict[curr]:
                if i not in v:
                    queue.append(i)
                    v.add(i)
dict = {}
with open("F:\CSE221\LAB\LAB4\input_task2.txt", "r") as file:
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
bfs(dict, 1)
