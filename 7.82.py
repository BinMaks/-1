n = int(input("Введите n: "))
a = [int(input(f"a[{i}]: ")) for i in range(n)]
pairs_equal = 0
pairs_zero = 0
pairs_even = 0
pairs_ends_5 = 0
for i in range(n - 1):
    if a[i] == a[i + 1]:
        pairs_equal += 1
    if a[i] == 0 and a[i + 1] == 0:
        pairs_zero += 1
    if a[i] % 2 == 0 and a[i + 1] % 2 == 0:
        pairs_even += 1
    if str(a[i]).endswith('5') and str(a[i + 1]).endswith('5'):
        pairs_ends_5 += 1
print(f"Пар равных чисел: {pairs_equal}")
print(f"Пар нулей: {pairs_zero}")
print(f"Пар чётных чисел: {pairs_even}")
print(f"Пар чисел, оканчивающихся на 5: {pairs_ends_5}")