file=open("F:\CSE221\LAB\LAB1\input1a.txt", "r") 
T = int(file.readline())
p
w=open("F:\CSE221\LAB\LAB1\output1a.txt","w")
for i in range(T):
    N=int(file.readline())
    if N % 2 == 0:
        w.write(f"{N} is an Even number\n")
    else:
        w.write(f"{N} is an Odd number\n")
w.close()
