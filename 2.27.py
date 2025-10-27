import math
a=float(input("Введите длину большего основания a:"))
b=float(input("введите длину меньшего основания b:"))
h=float(input("Введите длину h:"))
if a<=0 or b<=0:
    print("Основания должны быть положительными!")
elif a <= b:
    print("Большее основание a должно быть больше меньшего основания b!")
else:
    half_diff = (a-b)/2
    side = math.sqrt(half_diff**2+h**2)
    perimeter = a + b + 2*side
    print(f"Периметр трапеции: {perimeter:.2f} ед.")
