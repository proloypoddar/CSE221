def find_max(arr, start, end):
    if start == end:
        return arr[start]

    mid = (start + end) // 2

    left_max = find_max(arr, start, mid)
    right_max = find_max(arr, mid + 1, end)

    return left_max if left_max > right_max else right_max

file=open("F:\CSE221\LAB\LAB2\input_task4.txt","r")
N = int(file.readline())
line=file.readline()
array = list(map(int, line.split())) 

maximum = find_max(array, 0, N - 1)
w=open("F:\CSE221\LAB\LAB2\output_task4.txt","w")
value=str(maximum)
w.write(value)
w.close()
file.close()