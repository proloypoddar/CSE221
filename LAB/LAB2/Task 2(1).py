def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    return merge(left_sorted, right_sorted)


def merge(left, right):
    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged
file = open("F:\CSE221\LAB\LAB2\input_task2_1.txt", "r")
alice_length = int(file.readline())
alice_list = list(map(int, file.readline().split()))
bob_length = int(file.readline())
bob_list = list(map(int, file.readline().split()))
file.close()

merged_list = merge_sort(alice_list + bob_list)

output_file = open("F:\CSE221\LAB\LAB2\output_task2_1.txt", "w")
output_file.write(" ".join(map(str, merged_list)))
output_file.close()
