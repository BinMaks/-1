
c = [float(input(f"c[{i+1}] = ")) for i in range(16)]
greater_than_20 = [num for num in c if num > 20]
average = sum(greater_than_20) / len(greater_than_20)
print(f"Среднее арифметическое чисел > 20: {average}")