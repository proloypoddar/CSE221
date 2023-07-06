def find_max_value(arr, low, high):
    if low == high:
        return arr[low]
    mid = (low + high) // 2
    left_max = find_max_value(arr, low, mid)
    right_max = find_max_value(arr, mid + 1, high)
    if left_max > right_max:
        return left_max
    else:
        return right_max
input_file = 'F:\CSE221\LAB\LAB2\input_task4.txt'
with open(input_file, 'r') as file:
    N = int(file.readline())
    arr = list(map(int, file.readline().split()))
max_value = find_max_value(arr, 0, N - 1)
output_file = 'F:\CSE221\LAB\LAB2\output_task4.txt'
with open(output_file, 'w') as file:
    file.write("The maximum number is: " + str(max_value))
