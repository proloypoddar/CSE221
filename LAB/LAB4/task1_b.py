def adj_list(N, edges):
    adj_list = {i: [] for i in range(1, N + 1)}
    for u, v, w in edges:
        adj_list[u].append((v, w))
    return adj_list
with open('F:\CSE221\LAB\LAB4\input_task1_b.txt', 'r') as file:
    N, M = map(int, file.readline().split())
    edges = [tuple(map(int, file.readline().split())) for _ in range(M)]
adj_list = adj_list(N, edges)
with open('F:\CSE221\LAB\LAB4\output_task1_b.txt', 'w') as file:
    for i, j in adj_list.items():
        x = " ".join(f"({v},{w})" for v, w in j)
        file.write(f"{i} : {x}\n")
