def minCoins(coins, target):
    dp = [float('inf')] * (target + 1)
    dp[0] = 0
    for i in coins:
        for j in range(i, target + 1):
            dp[j] = min(dp[j], dp[j - i] + 1)
    return dp[target] if dp[target] != float('inf') else -1
with open("F:\CSE221\LAB\LAB8\input_task3.txt", "r") as file:
    N, X = map(int, file.readline().split())
    coin_denominations = list(map(int, file.readline().split()))
result = minCoins(coin_denominations, X)
with open("F:\CSE221\LAB\LAB8\output_task3.txt", "w") as file:
    file.write(str(result))
