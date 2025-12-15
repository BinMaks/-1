a, b, c = map(int, input("Введите три числа: ").split())
numbers = [a, b, c]
numbers.sort()
prod_two_smallest = numbers[0] * numbers[1]
print(f"Произведение двух наименьших: {prod_two_smallest}")