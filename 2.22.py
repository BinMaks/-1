import math
a=float(input("Введите первое число:"))
b=float(input("Введите второе число:"))
mod_a = abs(a)
mod_b = abs(b)
arithmetic_mean = (mod_a+mod_b)/2
geometric_mean=math.sqrt(mod_a*mod_b)
print(f"Среднее арифметическое модулей: {arithmetic_mean}")
print(f"Среднее геометрическое модулей: {geometric_mean}")

