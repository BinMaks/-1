a = int(input("Введите a: "))
b = int(input("Введите b: "))
quotient = 0
while a >= b:
    a -= b
    quotient += 1
print("Целочисленное деление:", quotient)
remainder = a
print("Остаток от деления:", remainder)