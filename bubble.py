def bubble_sort(arr):
    if len(arr)<=1:
        return arr
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
z=[5,8,6,7,3,6]
print(bubble_sort(z))