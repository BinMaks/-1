text = input("Введите текст: ")
if text.isdigit() or (text[0] == "-" and text[1:].isdigit()):
    print("Да")
else:
    print("Нет")