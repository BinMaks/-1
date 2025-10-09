import math
a=float(input("Введите значение a:"))
numerator = a**2+10
denominator = math.sqrt(a**2+1)
y=numerator/denominator
print(f" При a={a} значение функции y= {y:.4f}")