def inserction_sort(x):
    for i in range(0,len(x)):
        item=x[i]
        j=i-1
        while j>=0 and x[j]>item:
            x[j+1]=x[j]
            j=j-1
            x[j+1]=item
    return x
x=[4,8,6,4,1,2,4]
print(inserction_sort(x)) 