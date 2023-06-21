"""For the best case scenario it have to run O(n) 
Here is the code for O(n), If we use a veriable to compare variable  """
# def bubbleSort(arr):
#     for i in range(len(arr)-1):
#         for j in range(len(arr)-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr
"""This code are use O(n2) complextity, Lets make it O(n)"""
file = open("F:\CSE221\LAB\LAB1\input2.txt", "r")
T = int(file.readline())
arr = list(map(int, file.readline().split()))
file.close()
max_value = max(arr)
count = [0] * (max_value + 1)
for num in arr:
    count[num] += 1
output_file = open("F:\CSE221\LAB\LAB1\output2.txt", "w")
for i in range(len(count)):
    while count[i] > 0:
        output_file.write(str(i) + " ")
        count[i] -= 1
output_file.close()
