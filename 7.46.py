n = int(input("Введите n: "))
a = [int(input(f"a{i+1} = ")) for i in range(n)]
print("a₁ + aₙ =", a[0] + a[n-1])
print("a₂ - aₙ₋₁ =", a[1] - a[n-2])