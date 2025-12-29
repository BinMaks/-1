n = int(input("Введите число: "))
if n <= 1:
    print("Число не простое")
else:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Число простое")
    else:
        print("Число не простое")