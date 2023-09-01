out=open("F:\CSE221\LAB FINAL\output.txt","w")
visited=[]
queue=[]
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        out.write(m,end=" ")
        for i in graph[m]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
adj = {}  
lst=[]
file_path = "F:\CSE221\LAB FINAL\input.txt"
file=open(file_path, 'r')
line=file.readline()
lines = file.readlines()
for line in lines:
    nodes = line.strip( ).split() 
    for i in range(len(nodes)):
        lst.append(nodes)

lst2=[]
for i in lst:
    lst.append(i[1])
    adj[i[0]]=lst2

print(adj)
bfs(visited,adj,"1")
######################################
