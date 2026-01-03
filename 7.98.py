d = [int(input(f"d[{i}]: ")) for i in range(20)]
found = False
for i in range(len(d) - 1):
    if d[i] % 2 == 1 and d[i+1] % 2 == 1:  # оба нечётные
        print(f"Есть пара соседних нечетных чисел. Номера: {i+1} и {i+2}")
        found = True
        break
if not found:
    print("Пары соседних нечетных чисел нет")