import math
a=float(input("Введите длину меньшего основания a:"))
b=float(input("Введите длину большего основания b:"))
h=float(input("Введите высоту h:"))
c=math.sqrt(((b-a)/2**2+2**h))
perimeter=a+b+2*c
print(f"Периметр трапеции:{perimeter:.2f}")