a = list(map(int, input("Первое число (20 цифр): ")))
b = list(map(int, input("Второе число (20 цифр): ")))
result = [0] * 21
carry = 0
for i in range(19, -1, -1):
    s = a[i] + b[i] + carry
    result[i + 1] = s % 10
    carry = s // 10
result[0] = carry
print("Сумма:", ''.join(map(str, result)).lstrip('0') or '0')


a = list(map(int, input("Уменьшаемое (30 цифр): ")))
b = list(map(int, input("Вычитаемое (30 цифр): ")))
result = [0] * 30
borrow = 0
for i in range(29, -1, -1):
    diff = a[i] - b[i] - borrow
    if diff < 0:
        diff += 10
        borrow = 1
    else:
        borrow = 0
    result[i] = diff
print("Разность:", ''.join(map(str, result)).lstrip('0') or '0')