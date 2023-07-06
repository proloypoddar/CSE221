"""For the best case scenario it have to run O(n) 
Here is the code for O(n), If we use a Flag variable  """

def bubbleSort(T,arr):
    T = len(arr)
    for i in range(T-1):
        flag = False
        for j in range(T-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True
        if not flag:
            break
    return arr
file = open("F:\\CSE221\\LAB\\LAB1\\input2.txt", "r")
T = list(map(int, file.readline().split()))
arr = list(map(int, file.readline().split()))
file.close()
array = bubbleSort(T,arr)
w = open("F:\\CSE221\\LAB\\LAB1\\output2.txt", "w")
w.write(" ".join(map(str, array)))
w.close()
