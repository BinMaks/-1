k = int(input("Введите k (1 <= k <= 252): "))
sequence = ''.join(str(i) for i in range (50, 251))
print(f"k-я цифра: {sequence[k-1]}")