n = int(input("Введите число n: "))
a = [int(input(f"a[{i+1}] = ")) for i in range(12)]
greater_than_n = [num for num in a if num > n]
if greater_than_n:
    average = sum(greater_than_n) / len(greater_than_n)
    print(f"Среднее арифметическое чисел > {n}: {average}")
else:
    print(f"Чисел, больших {n}, нет")