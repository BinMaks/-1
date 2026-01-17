number = input("Введите положительное вещественное число: ")
dot_pos = number.find('.')
if dot_pos != -1:
    integer_part = number[:dot_pos]
    fractional_part = number[dot_pos+1:]
else:
    integer_part = number
    fractional_part = ""
print("Количество цифр в целой части:", len(integer_part))
print("Количество цифр в дробной части:", len(fractional_part))