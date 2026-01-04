b = [float(input(f"b[{i+1}] = ")) for i in range(15)]
greater_than_10 = [num for num in b if num > 10]
if greater_than_10:
    average = sum(greater_than_10) / len(greater_than_10)
    print(f"Среднее арифметическое чисел > 10: {average}")
else:
    print("Чисел, больших 10, нет")