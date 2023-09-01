def climb_stairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    stp = [0] * (n + 1)
    stp[1] = 1
    stp[2] = 2

    for i in range(3, n + 1):
        stp[i] = stp[i - 1] + stp[i - 2]
    return stp[n]
with open("F:\CSE221\LAB\LAB8\input_task2.txt", "r") as file:
    N = int(file.readline().strip())
x = climb_stairs(N)
with open("F:\CSE221\LAB\LAB8\output_task2.txt", "w") as file:
    file.write(str(x))
