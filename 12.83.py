sentence = input("Введите предложение: ").lower()
if 'а' in sentence:
    first_pos = sentence.find('а')
    print("Буква 'а' есть в предложении. Порядковый номер первой 'а':", first_pos + 1)
else:
    print("Буквы 'а' в предложении нет")