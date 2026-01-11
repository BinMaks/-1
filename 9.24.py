
a, b = map(int, input("Введите a, b: ").split())
max_divs = 0
max_num = a
for num in range(a, b + 1):
    divs = len([i for i in range(1, num + 1) if num % i == 0])
    if divs > max_divs:
        max_divs = divs
        max_num = num
print(f"Число с макс. делителями: {max_num} ({max_divs} делителей)")