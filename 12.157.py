text = input("Введите текст: ")
max_count = 0
current_count = 0
for char in text:
    if char.isdigit():
        current_count += 1
        max_count = max(max_count, current_count)
    else:
        current_count = 0
print("Максимальное количество подряд идущих цифр:", max_count)