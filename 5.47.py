n = int(input("Введите n (n > 4): "))
v = [0, 0, 1.5, 1.5]
for i in range(4, n + 1):
    v_i = v[i-1] - v[i-2] + v[i-3]
    v.append(v_i)
print(f"v_n: {v[n]}")