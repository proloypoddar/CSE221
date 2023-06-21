arr=[1,7,13,4,5,7,13,12]
N=len(arr)
maxValue = arr[0]
for i in range(1,N):
    if maxValue < arr[i]:
        maxValue = arr[i]
print(maxValue)
I#Time complexity O(n)