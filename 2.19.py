import math
a=float(input("Введите значение a:"))
b=float(input("Введите значение b:"))
if b<=0:
    print("Значение b должно быть больше нуля.")
else:
    numerator_x=(2/(a**2+25))+b
    denominator_x=math.sqrt(b)+(a+b)/2
    x=numerator_x/denominator_x
    numerator_y=abs(a)+2*math.sin(b)
    denominator_y=5.5*a
    y=numerator_y/denominator_y
    print(f"x={x}")
    print(f"y={y}")