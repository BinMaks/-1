
numbers = []
while True:
    num = int(input("Число (окончание ввода — -1): "))
    if num == -1:
        break
    numbers.append(num)

found = False
for i in range(len(numbers) - 1):
    if numbers[i] == numbers[i+1]:
        print(f"Есть пара одинаковых соседних чисел. Номера: {i+1} и {i+2}")
        found = True
        break
if not found:
    print("Пары одинаковых соседних чисел нет")