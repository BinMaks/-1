n = int(input("Введите n: "))
a = [int(input(f"a[{i}]: ")) for i in range(n)]
has_even = any(x % 2 == 0 for x in a)
print("Есть четное число" if has_even else "Четных чисел нет")