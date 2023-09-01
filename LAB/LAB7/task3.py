def friend(frnd_circles, i):
    if frnd_circles[i] == i:
        return i
    frnd_circles[i] = friend(frnd_circles, frnd_circles[i])
    return frnd_circles[i]

def union(frnd_circles, sizes, i, j):
    root_i = friend(frnd_circles, i)
    root_j = friend(frnd_circles, j)
    if root_i != root_j:
        frnd_circles[root_i] = root_j
        sizes[root_j] += sizes[root_i]


input_file = "F:\CSE221\LAB\LAB7\input_task3.txt"  
output_file = "F:\CSE221\LAB\LAB7\output_task3.txt" 

with open(input_file, "r") as inp, open(output_file, "w") as out:
    n, k = map(int, inp.readline().split())
    frnd_circles = [i for i in range(n)]
    sizes = [1] * n
    for _ in range(k):
        a, b = map(int, inp.readline().split())
        union(frnd_circles, sizes, a - 1, b - 1)
        out.write(str(sizes[friend(frnd_circles, a - 1)]) + '\n')
