# file1=open("F:\CSE221\LAB\input1a.txt","w")
# p="Hello"
# file1.writelines(p)
# file1.close()
# ################
file1=open("F:\CSE221\LAB\input1a.txt","r")
# var=int(file1.readlines())
# int=[]
# for i in range(var):
#     int.append(file1.readline())
# print(int)
var=file1.read()
print(var)
out=var.split("\n")
print(out)