expression = input("Введите выражение (например, '1+25+3'): ")
numbers = [int(x) for x in expression.split('+')]
print("Сумма:", sum(numbers))