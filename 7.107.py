n = int(input("Введите число n: "))
a = [int(input(f"a[{i+1}] = ")) for i in range(12)]
greater_than_n = [num for num in a if num > n]
average = sum(greater_than_n) / len(greater_than_n)
print(f"Среднее арифметическое чисел > {n}: {average}")