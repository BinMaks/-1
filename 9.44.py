def count_weight_combinations(v, weights):
    dp = [0] * (v + 1)
    dp[0] = 1
    for w in weights:
        for i in range(w, v + 1):
            dp[i] += dp[i - w]
    return dp[v]

weights = [100, 200, 300, 500, 1000, 1200, 1400, 1500, 2000, 3000]
v = int(input("Вес v: "))
print("Способов:", count_weight_combinations(v, weights))