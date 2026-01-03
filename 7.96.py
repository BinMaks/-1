a = [int(input(f"a[{i}]: ")) for i in range(15)]
found = False
for i in range(len(a) - 1):
    if a[i] == a[i+1]:
        print(f"Есть пара одинаковых соседних чисел. Номера: {i+1} и {i+2}")
        found = True
        break
if not found:
    print("Пары одинаковых соседних чисел нет")