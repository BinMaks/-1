import math
e=float(input("Введите значение e:"))
f=float(input("Введите значение f:"))
g=float(input("Введите значение g:"))
h=float(input("Введите значение h:"))
a=(e+f/2)/3
b=abs(h**2-g)
c=math.sqrt((g-h)**2-3*math.sin(e))
print(f"a={a}")
print(f"b={b}")
print(f"c={c}")
