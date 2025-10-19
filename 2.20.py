import math
def calculate_functions(e,f,g,h):
    if f==0 or (e*f-3)==0:
        return "Ошибка: деление на ноль"
    a=math.sqrt(abs(e-3/f)**3+g)
    b=math.sin(e)+math.cos(h)**2
    c=33*g/(e*f-3)
    return a,b,c
e=float(input("Введите значение e:"))
f=float(input("Введите значение f:"))
g=float(input("Введите значение g:"))
h=float(input("Введите значение h:"))
result=calculate_functions(e,f, g, h)
if isinstance(result,str):
    print(result)
else:
    a,b,c=result
    print(f"a={a}, b={b}, c={c}")
