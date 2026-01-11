def count_ways(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    coins = [1, 2, 5, 10]
    for coin in coins:
        for i in range(coin, n + 1):
            dp[i] += dp[i - coin]
    return dp[n]
def find_all_ways(n):
    ways = [[] for _ in range(n + 1)]
    ways[0] = [[]]
    coins = [1, 2, 5, 10]

    for coin in coins:
        for i in range(coin, n + 1):
            for prev in ways[i - coin]:
                ways[i].append(prev + [coin])
    return ways[n]
n = int(input("Введите сумму (n < 100): "))
print(f"Количество способов: {count_ways(n)}")
print("Все способы:")
for way in find_all_ways(n):
    print(way)