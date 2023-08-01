def dfs(tree, curr, root, v):
    v.add(curr)
    for i in tree[curr]:
        if i not in v:
            if dfs(tree, i, curr, v):
                return True
        elif i != root:
            return True
    return False
def cycle(tree):
    v = set()
    for i in tree:
        if i not in v:
            if dfs(tree, i, None, v):
                return True
    return False
dict = {}
with open("F:\CSE221\LAB\LAB4\input_task4.txt", "r") as file:
    lines = file.readlines()[1:]
    data = [list(map(int, line.split())) for line in lines]

for i in data:
    a, b = i
    if a not in dict:
        dict[a] = []
    if b not in dict:
        dict[b] = []
    dict[a].append(b)
    dict[b].append(a)
has_cycle_result = cycle(dict)
with open("F:\CSE221\LAB\LAB4\output_task4.txt","w")as file2:
    if has_cycle_result:
        file2.write("YES")
    else:
        file2.write("NO")
        
