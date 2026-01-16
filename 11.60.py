arr = [int(x) for x in input("Введите элементы массива: ").split()]
divisor = int(input("Введите число для проверки кратности: "))

sum_odd = sum(x for x in arr if x % 2 != 0)
print(f"Сумма нечетных элементов: {sum_odd}")

sum_divisible = sum(x for x in arr if x % divisor == 0)
print(f"Сумма элементов, кратных {divisor}: {sum_divisible}")

a, b = map(int, input("Введите a и b: ").split())
sum_divisible_a_or_b = sum(x for x in arr if x % a == 0 or x % b == 0)
print(f"Сумма элементов, кратных {a} или {b}: {sum_divisible_a_or_b}")