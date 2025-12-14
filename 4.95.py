n = int(input("введите н (1 <= н <= 32: "))
sequence = '0' + ''.join(str(i) for i in range (1,21))
print(f"Цифра с номером {n}: {sequence[n-1]}")