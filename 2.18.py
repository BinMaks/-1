import math
def calculate_functions(x,y):
    numerator_z = x+(2+y)/(x**2)
    denominator_z= y+1/math.sqrt(x**2+10)
    z= numerator_z/denominator_z
    q=7.25*math.sin(x)-abs(y)
    return z,q
x=float(input("Введите значение x:"))
y=float(input("Введите значение y:"))
z,q=calculate_functions(x, y)
print(f"Значение z:{z}")
print(f"Значение q:{q}")