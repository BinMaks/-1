a=float(input("Введите первое число:"))
b=float(input("Введите второе число:"))
sum_result=a+b
diff_result=a-b
prod_result=a*b
if b != 0:
    div_result=a/b
else:
    div_result = "Ошибка: деление на ноль невозможно"
print(f"Сумма: {sum_result}")
print(f"Разность: {diff_result}")
print(f"Произведение: {prod_result}")
print(f"Частное: {div_result}")
