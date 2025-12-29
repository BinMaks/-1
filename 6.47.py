a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
print("Простые числа в диапазоне:")
for num in range(a, b + 1):
    if is_prime(num):
        print(num, end=" ")