k = int(input("Введите k (1 <= k <= 180): "))
sequence = ''.join(str(i) for i in range (10, 100))
print(f"k-я цифра: {sequence[k - 1]}")