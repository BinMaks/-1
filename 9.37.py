
def are_coprime(a, b):
    return (a, b) == 1

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if are_coprime(a, b):
    print("Числа взаимно простые")
else:
    print("Числа не взаимно простые")