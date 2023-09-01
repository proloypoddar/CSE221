def find(prnt, i):
    if prnt[i] == i:
        return i
    return find(prnt, prnt[i])
def union(prnt, rank, u, v):
    u = find(prnt, u)
    v = find(prnt, v)
    if rank[u] < rank[v]:
        prnt[u] = v
    elif rank[u] > rank[v]:
        prnt[v] = u
    else:
        prnt[v] = u
        rank[u] += 1
def minimum_cost(N, path):
    path.sort(key=lambda x: x[2])
    
    prnt = list(range(N + 1))
    rank = [0] * (N + 1)
    min_cost = 0
    
    for i in path:
        u, v, w = i
        u = find(prnt, u)
        v = find(prnt, v)
        
        if u != v:
            min_cost += w
            union(prnt, rank, u, v)
    return min_cost
with open("F:\CSE221\LAB\LAB8\input_task1.txt", "r") as file:
    N, M = map(int, file.readline().split())
    path = []
    for _ in range(M):
        u, v, w = map(int, file.readline().split())
        path.append((u, v, w))
result = minimum_cost(N, path)

with open("F:\CSE221\LAB\LAB8\output_task1.txt", "w") as file:
    file.write(str(result))
