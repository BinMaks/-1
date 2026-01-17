text = input("Введите текст: ")
count = sum(1 for char in text if char.isdigit())
print(count)