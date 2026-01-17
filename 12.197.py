expression = input("Введите арифметическое выражение: ")
stack = []
for i, char in enumerate(expression):
    if char == '(':
        stack.append(i)
    elif char == ')':
        if not stack:
            print(f"Ошибка: лишняя закрывающая скобка на позиции {i}")
            break
        stack.pop()
else:
    if stack:
        print(f"Ошибка: лишние открывающие скобки, количество: {len(stack)}")
    else:
        print("Скобки расставлены правильно")