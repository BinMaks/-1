import math
a=float(input("Введите первое число:"))
b=float(input("Введите второе число:"))
avg_arithmetic=(a+b)/2
avg_geometric=math.sqrt(a*b)
print(f"Среднее арифметическое:{avg_arithmetic}")
print(f"Среднее геометрическое:{avg_geometric}")