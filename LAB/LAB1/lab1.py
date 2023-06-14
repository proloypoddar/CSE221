file=open("F:\CSE221\LAB\input1a.txt", "r") 
lines = file.readlines()

T = int(lines[0].strip())

lst = []
for line in lines[1:]:
    N = int(line.strip())
    lst.append(N)

w = open("F:\CSE221\LAB\output1a.txt", "w")
for i in lst:
    if i % 2 == 0:
        w.write(f"{i} is an Even number\n")
    else:
        w.write(f"{i} is an Odd number\n")
w.close()
