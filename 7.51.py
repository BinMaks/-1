
numbers = []
while True:
    num = int(input("Число (0 — завершить): "))
    if num == 0:
        break
    numbers.append(num)
sum_odd = 0
for num in numbers:
    if num % 2 == 1:
        sum_odd += num
    else:
        break
print("Сумма нечетных чисел в начале:", sum_odd)