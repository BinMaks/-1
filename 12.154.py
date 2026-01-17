expression = input("Введите выражение (например, '3+5+7'): ")
digits = [int(x) for x in expression.split("+")]
print("Сумма:", sum(digits))