a = float(input("Коэффициент a: "))
b = float(input("Коэффициент b: "))
c = float(input("Коэффициент с: "))
discriminant = b ** 2 - 4 * a * c
if discriminant >= 0:
    print("Уравнение имеет корни. ")
else:
    print("Уравнение не имеет действительных корней. ")
    