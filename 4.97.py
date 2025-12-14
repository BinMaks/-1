k = int(input("Введите k (1 <= k <= 222): "))
sequence = ''.join(str(i) for i in range (1, 111))
print(f"k-я цифра: {sequence[k-1]}")