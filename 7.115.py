n = int(input("Введите число n: "))
m = int(input("Введите количество чисел m: "))
a = [int(input(f"a[{i+1}] = ")) for i in range(m)]
divisible_by_n = [num for num in a if num % n == 0]
if divisible_by_n:
    average = sum(divisible_by_n) / len(divisible_by_n)
    print(f"Среднее арифметическое чисел, кратных {n}: {average}")
else:
    print(f"Чисел, кратных {n}, нет")