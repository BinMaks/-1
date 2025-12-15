a, b, c = map(int, input("Введите три числа: ").split())
numbers = [a, b, c]
numbers.sort()
sum_two_largest = numbers[1] + numbers[2]
print(f"Сумма двух наибольших: {sum_two_largest}")