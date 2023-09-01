
visited=[]
queue=[]
def bfs(visited,graph,node):
    visited.append(node)
    print(node,end=" ")
    for i in graph[node]:
        if i not in visited:
            bfs(visited,graph,i)
adj={}
file=open("F:\CSE221\PRACTICE\input.txt",'r')
l=file.readlines()
for i in l:
    nodes=i.strip().split()
    if nodes:
        adj[nodes[0]]=nodes[1: ]
print(adj)

bfs(visited,adj,"A")
        
    

