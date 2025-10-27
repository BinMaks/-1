import math

a=float(input("Введите длину большего основания a:"))
b=float(input("Введите длину меньшего основания b:"))
alpha_deg = float(input("Введите угол при большем основании (в градусах):"))
if a<=0 or b<=0:
    print("Основания должны быть положительными!")
elif a<=b:
    print("Большее основание a должно быть больше меньшего основания b!")
else:
    alpha_rad=math.radians(alpha_deg)
    area=(a**2-b**2)*math.tan(alpha_rad)/4
    print(f"Площадь трапеции: {area:.2f} кв.ед")