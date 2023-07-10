def max_value(N, A):
    val = 0

    for i in range(N):
        for j in range(i + 1, N):
            value = A[i] + A[j]**2
            if value > val:
                val = value
    return val

input_file = open("F:\CSE221\LAB\LAB3\input_task2.txt", "r")
output_file = open("F:\CSE221\LAB\LAB3\output_task2.txt", "w")

N = int(input_file.readline())
line = input_file.readline().strip()
A = [int(x) for x in line.split()]

result = max_value(N, A)
output_file.write(str(result))

input_file.close()
output_file.close()
