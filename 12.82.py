sentence = input("Введите предложение: ").lower()
positions = [i for i, char in enumerate(sentence) if char == 'е']
if positions:
    print("Порядковый номер первой 'е':", positions[0] + 1)
    print("Порядковый номер последней 'е':", positions[-1] + 1)
else:
    print("Буквы 'е' в предложении нет")