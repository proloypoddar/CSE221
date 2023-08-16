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
N = int(input("Enter Stair: "))
x = climb_stairs(N)
print(x)

