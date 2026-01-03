numbers = []
while True:
    num = float(input("Число (0 для завершения): "))
    if num == 0:
        break
    numbers.append(num)
count_before_zero = len(numbers)
print("Чисел до первого нуля:", count_before_zero)