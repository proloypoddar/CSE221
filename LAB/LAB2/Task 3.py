def marge(x):
    if len(x)<=1:
        return x
    mid=len(x)//2
    array_1=x[:mid]
    array_2=x[mid:]
    marge(array_1)
    marge(array_2)
    i=j=k=0

    while i<len(array_1) and j<len(array_2):
        if array_1[i]<array_2[j]:
            x[k]=array_1[i]
            i+=1
        else:
            x[k]=array_2[j]
            j+=1
        k+=1
    while i< len(array_1):
        x[k]=array_1[i]
        k+=1
        i+=1
    while j<len(array_2):
        x[k]=array_2[j]
        k+=1
        j+=1
    return x
x=[]
i=int(input())
for i in range(0,i):
    i=int(input())
    x.append(i)

print(marge(x))

