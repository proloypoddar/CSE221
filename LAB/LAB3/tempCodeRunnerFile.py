def max_value(N, A):
    val = 0

    for i in range(N):
        for j in range(i + 1, N):
            value = A[i] + A[j]**2
            if value > val:
                val = value
    return val
