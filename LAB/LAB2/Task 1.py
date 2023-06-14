def is_sum_possible(lst, S):
    seen = set()
    for num in lst:
        if S - num in seen:
            return True
        seen.add(num)
    return False

# Example usage
N = int(input("Enter the number of integers: "))
lst = []
for _ in range(N):
    num = int(input("Enter an integer: "))
    lst.append(num)

S = int(input("Enter the target sum: "))

result = is_sum_possible(lst, S)
if result:
    print("It is possible to find two values with the given sum.")
else:
    print("It is not possible to find two values with the given sum.")
