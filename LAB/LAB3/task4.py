def partition(arr, low, high):
    p = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= p:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_select(arr, low, high, k):
    if low == high:
        return arr[low]

    p_idx = partition(arr, low, high)

    if p_idx == k - 1:
        return arr[p_idx]
    elif p_idx > k - 1:
        return quick_select(arr, low, p_idx - 1, k)
    else:
        return quick_select(arr, p_idx + 1, high, k)

input_file = open("F:/CSE221/LAB/LAB3/input_task4.txt", "r")
output_file = open("F:/CSE221/LAB/LAB3/output_task4.txt", "w")

N = int(input_file.readline().strip())
line = input_file.readline().strip()
arr = [int(x) for x in line.split()]
Q = int(input_file.readline().strip())

for i in range(Q):
    K = int(input_file.readline().strip())
    result = quick_select(arr, 0, N - 1, K)
    output_file.write(str(result) + "\n")

input_file.close()
output_file.close()
