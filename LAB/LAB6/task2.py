import heapq

def meet(graph, N, S, T):
    dis_Alice = [float('inf')] * (N + 1)
    dis_Bob = [float('inf')] * (N + 1)
    dis_Alice[S] = 0
    dis_Bob[T] = 0
    pq_Alice = [(0, S)]
    pq_Bob = [(0, T)] 
    while pq_Alice or pq_Bob:
        if pq_Alice:
            dist, node = heapq.heappop(pq_Alice)
            distances = dis_Alice
        else:
            dist, node = heapq.heappop(pq_Bob)
            distances = dis_Bob
        
        if dist > distances[node]:
            continue
        
        for i, j in graph[node]:
            new_dist = dist + j
            
            if new_dist < distances[i]:
                distances[i] = new_dist
                if distances is dis_Alice:
                    heapq.heappush(pq_Alice, (new_dist, i))
                else:
                    heapq.heappush(pq_Bob, (new_dist, i))
    
    m_time = float('inf')
    m_node = None

    for node in range(1, N + 1):
        if dis_Alice[node] != float('inf') and dis_Bob[node] != float('inf'):
            total_time = max(dis_Alice[node], dis_Bob[node])
            if total_time < m_time:
                m_time = total_time
                m_node = node
    
    return m_time, m_node

file = open("F:\CSE221\LAB\LAB6\input_task2.txt", "r")
lines = file.readlines()
file.close()
N, E = map(int, lines[0].split())
graph=[]
for i in range(N+1):
    graph.append([])
for i in range(1, E + 1):
    u, v, w = map(int, lines[i].split())
    graph[u].append((v, w))
S, T = map(int, lines[E + 1].split())
m_time, m_node = meet(graph, N, S, T)
file2 = open("F:\CSE221\LAB\LAB6\output_task2.txt", "w")
if m_time == float('inf'):
    file2.write("Impossible\n")
else:
    file2.write(f"Time {m_time}\n")
    file2.write(f"Node {m_node}\n")
file2.close()
