def quicksort(x):
    if len(x)<=1:
        return x
    else:
        pivot=x[0]
        less=[i for i in x[1:] if i<=pivot]
        grate=[i for i in x[1:] if i>=pivot]
        return quicksort(less)+[pivot]+quicksort(grate)
x=[1,3,23,42,5,6,7,783,2,4,3,42,2,246,9]
print(quicksort(x))