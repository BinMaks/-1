text = input("Введите текст: ")
found = False
for i in range(len(text) - 4):
    if text[i] == text[i+1] == text[i+2] == text[i+3] == text[i+4]:
        found = True
        break
if found:
    print("В тексте есть пять идущих подряд одинаковых символов")
else:
    print("В тексте нет пяти идущих подряд одинаковых символов")