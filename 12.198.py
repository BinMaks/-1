text = input("Введите текст: ")
target_length = int(input("Введите требуемую длину строки: "))
words = text.split()
if len(text) >= target_length:
    print("Исходная длина строки больше или равна требуемой.")
else:
    spaces_needed = target_length - len(text)
    gaps = len(words) - 1
    if gaps == 0:
        print(text)
    else:
        base_spaces = spaces_needed // gaps
        extra_spaces = spaces_needed % gaps
        result = words[0]
        for i in range(1, len(words)):
            spaces = base_spaces + (1 if i <= extra_spaces else 0)
            result += ' ' * spaces + words[i]
        print(result)