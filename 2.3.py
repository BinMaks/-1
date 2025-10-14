import math
def calculate_function_a(a):
    numerator =2*a+math.sin(abs(3*a))
    denominator = 3.56
    result = math.sqrt(numerator/denominator)
    return result
a= float(input("Введите значение a:"))
result=calculate_function_a(a)
print(f"Значение функции:{result}")


import math
def calculate_function_b(x):
    numerator=3.2+math.sqrt(1+x)
    denominator=15*abs(x)
    result=math.sin(numerator/denominator)
    return result
x=float(input("Введите значение x:"))
result=calculate_function_b(x)
print(f"Значение функции:{result}")