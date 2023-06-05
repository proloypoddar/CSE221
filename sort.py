def selection(x):
    if len(x)<=1:
        return x
    value=0
    for i in range(1,len(x)):
        if x[i]<x[value]:
            value=i
    x[0], x[value] = x[value], x[0]
    return [x[0]]+selection(x[1:])
z=[5,9,7,6,4]
print(selection(z))