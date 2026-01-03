numbers = []
while True:
    num = int(input("Число (окончание ввода — 9999): "))
    if num == 9999:
        break
    numbers.append(num)

found = False
for i in range(len(numbers) - 1):
    if numbers[i] % 2 == 0 and numbers[i+1] % 2 == 0:  # оба чётные
        print(f"Есть пара соседних четных чисел. Номера: {i+1} и {i+2}")
        found = True
        break
if not found:
    print("Пары соседних четных чисел нет")