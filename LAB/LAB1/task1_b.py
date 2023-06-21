file=open("F:\CSE221\LAB\LAB1\input1b.txt","r")
w=open("F:\CSE221\LAB\LAB1\output1b.txt","w")
T = int(file.readline())
for i in range(T):
    x=(file.readline())
    exp=x.split()
    if exp[2]=="+":
        m=int(exp[1])+int(exp[3])
        w.write(f"The result of {exp[1]} {exp[2]} {exp[3]} is {m}\n")
    if exp[2]=="-":
        m=int(exp[1])-int(exp[3])
        w.write(f"The result of {exp[1]} {exp[2]} {exp[3]} is {m}\n")
    if exp[2]=="/":
        m=int(exp[1])/int(exp[3])
        w.write(f"The result of {exp[1]} {exp[2]} {exp[3]} is {m}\n")
    if exp[2]=="*":
        m=int(exp[1])*int(exp[3])
        w.write(f"The result of {exp[1]} {exp[2]} {exp[3]} is {m}\n")
file.close()
w.close()