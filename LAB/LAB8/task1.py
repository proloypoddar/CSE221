def find(parent, node):
    if parent[node] == node:
        return node
    parent[node] = find(parent, parent[node])
    return parent[node]
def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)
    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1
def kruskal(edges, N):
    parent = [i for i in range(N + 1)]
    rank = [0] * (N + 1)
    edges.sort(key=lambda edge: edge[2])
    total_cost = 0
    for edge in edges:
        u, v, w = edge
        u_root = find(parent, u)
        v_root = find(parent, v)

        if u_root != v_root:
            union(parent, rank, u_root, v_root)
        else:
            total_cost += w
    return total_cost
N, M = map(int, input().split())
edges = []
for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))
total_maintenance_cost = kruskal(edges, N)
print(total_maintenance_cost)
