text = input("Введите предложение: ")
max_spaces = 0
current_spaces = 0
for char in text:
    if char == ' ':
        current_spaces += 1
        max_spaces = max(max_spaces, current_spaces)
    else:
        current_spaces = 0
print("Наибольшее количество идущих подряд пробелов:", max_spaces)