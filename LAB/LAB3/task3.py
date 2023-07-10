def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

input_file = open("F:/CSE221/LAB/LAB3/input_task3.txt", "r")
output_file = open("F:/CSE221/LAB/LAB3/output_task3.txt", "w")

N = int(input_file.readline())
line = input_file.readline().strip()
arr = [int(x) for x in line.split()]

quickSort(arr, 0, N - 1)

output_str = ""
for i in range(N):
    if i > 0:
        output_str += " "
    output_str += str(arr[i])

output_file.write(output_str)

input_file.close()
output_file.close()
