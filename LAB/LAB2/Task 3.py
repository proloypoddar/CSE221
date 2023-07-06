def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    l = 0
    r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1

    while l < len(left):
        merged.append(left[l])
        l += 1

    while r < len(right):
        merged.append(right[r])
        r += 1

    return merged

file = open("F:\CSE221\LAB\LAB2\input_task3.txt", "r")
N=file.readline()
line = file.readline()
array = list(map(int, line.split()))
file.close()
sorted_array = merge_sort(array)
w = open("F:\CSE221\LAB\LAB2\output_task3.txt", "w")
w.write(" ".join(map(str, sorted_array)))
w.close()
