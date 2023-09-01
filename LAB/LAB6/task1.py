import heapq

def dijkstra(graph, N, s):
    distance = [float("inf")] * (N + 1)
    distance[s] = 0
    pq = [(0, s)]
    while pq:
        dist, node = heapq.heappop(pq)
        if dist > distance[node]:
            continue
        for i, j in graph[node]:
            new_dis = dist + j
            if new_dis < distance[i]:
                distance[i] = new_dis
                heapq.heappush(pq, (new_dis, i))
    return distance[1:]

file = open("F:\CSE221\LAB\LAB6\input_task1.txt", "r")
lines = file.readlines()
file.close()

N, M = map(int, lines[0].split())
graph = [[] for _ in range(N + 1)]

for i in range(1, M + 1):
    u, v, w = map(int, lines[i].split())
    graph[u].append((v, w))

s = int(lines[M + 1].strip())  
djk = dijkstra(graph, N, s)

file2 = open("F:\CSE221\LAB\LAB6\output_task1.txt", "w")
for i in djk:
    if i == float("inf"):
        file2.write("-1\n")  
    else:
        s = str(i)
        file2.write(s+" ")
file2.close()
