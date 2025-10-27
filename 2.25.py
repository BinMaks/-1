a=float(input("Введите длину стороны a:"))
b=float(input("Введите длину стороны b:"))
c=float(input("Введите длину высоту c:"))
volume = a*b*c
lateral_surface_area=2*c*(a+b)
print(f"Объём параллелепипеда: {volume} куб.ед")
print(f"Площадь боковой поверхности: {lateral_surface_area} кв.ед")
