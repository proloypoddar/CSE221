out=open("F:\CSE221\PRACTICE\output.txt","w")
visited=[]
queue=[]
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        out.write(m)
        for i in graph[m]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

adj = {}  
file_path = "F:\CSE221\PRACTICE\input.txt"
file=open(file_path, 'r')
lines = file.readlines()
for line in lines:
    nodes = line.strip().split()  
    if nodes:
        adj[nodes[0]] = nodes[1: ] 

bfs(visited,adj,"A")