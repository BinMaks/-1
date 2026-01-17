text = input("Введите текст: ")
max_count = 0
current_count = 1
for i in range(1, len(text)):
    if text[i] == text[i-1]:
        current_count += 1
        max_count = max(max_count, current_count)
    else:
        current_count = 1
print("Наибольшее количество идущих подряд одинаковых символов:", max_count)