text = input("Введите текст: ")
stack = []
for i, char in enumerate(text):
    if char == '(':
        stack.append(i)
    elif char == ')':
        if not stack:
            print(f"Лишняя закрывающая скобка на позиции {i}")
            break
        stack.pop()
else:
    if stack:
        print(f"Лишние открывающие скобки, количество: {len(stack)}")
    else:
        print("Скобки расставлены правильно")