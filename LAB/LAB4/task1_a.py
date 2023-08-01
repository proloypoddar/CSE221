
def matrix(N, M, edges):
    matrix = [[0] * (N + 1) for _ in range(N + 1)]
    for u, v, w in edges:
        matrix[u][v] = w
    return matrix
with open('F:\CSE221\LAB\LAB4\input_task1_a.txt', 'r') as file:
    N, M = map(int, file.readline().split())
    edges = [tuple(map(int, file.readline().split())) for _ in range(M)]
adj = matrix(N, M, edges)
with open('F:\CSE221\LAB\LAB4\output_task1_a.txt', 'w') as file:
    for i in adj[1:]: 
        file.write(" ".join(map(str, i[1:])) + "\n")
