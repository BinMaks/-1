def calculate_z(x,y):
    z=2*x**3-3.44*x*y+2.3*x**2-7.1*y+2
    return z
x=float(input("Введите значение x:"))
y=float(input("Введите значение y:"))
result_z=calculate_z(x,y)
print(f"Значение функции z={result_z:.2f}")