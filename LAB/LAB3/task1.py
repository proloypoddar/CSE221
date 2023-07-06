def count_pairs(n, heights):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if heights[i] > heights[j]:
                count += 1
    return count

# Read input
N = int(input())
heights = list(map(int, input().split()))

# Count the number of pairs
total_pairs = count_pairs(N, heights)

# Print the result
print(total_pairs)
a=5
b=5,4,3,2,1
count_pairs(b,a)