import heapq
def safe_path(graph, N):
    distances = [float('inf')] * (N + 1)
    distances[1] = 0
    visited = [False] * (N + 1)
    pq = [(0, 1)]

    while pq:
        dist, node = heapq.heappop(pq)
        if visited[node]:
            continue
        visited[node] = True
        for i, j in graph[node]:
            new_dist = max(distances[node], j)
            
            if new_dist < distances[i]:
                distances[i] = new_dist
                heapq.heappush(pq, (new_dist, i))
    return distances[N]

file = open("F:\CSE221\LAB\LAB6\input_task3.txt", "r")
lines = file.readlines()
file.close()
file2=open("F:\CSE221\LAB\LAB6\output_task3.txt", "w")
N, M = map(int, lines[0].split())
graph = [[] for _ in range(N + 1)]
for i in range(1, M + 1):
    u, v, w = map(int, lines[i].split())
    graph[u].append((v, w))
path = safe_path(graph, N)

if path == float('inf'):
    file2.write("Impossible")
else:
    file2.write(str(path))
