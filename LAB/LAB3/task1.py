def merge(arr, left, mid, right):
    count = 0

    i = left
    j = mid + 1
    k = left
    temp = [0] * (right + 1)

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            count += mid - i + 1
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    for idx in range(left, right + 1):
        arr[idx] = temp[idx]

    return count

def merge_sort(arr, left, right):
    count = 0

    if left < right:
        mid = (left + right) // 2
        count += merge_sort(arr, left, mid)
        count += merge_sort(arr, mid + 1, right)
        count += merge(arr, left, mid, right)

    return count

input_file = open("F:\CSE221\LAB\LAB3\input_task1.txt", "r")
output_file = open("F:\CSE221\LAB\LAB3\output_task1.txt", "w")

N = int(input_file.readline())
line = input_file.readline().strip()
A = list(map(int, line.split()))

result = merge_sort(A, 0, N - 1)
output_file.write(str(result))

input_file.close()
output_file.close()
