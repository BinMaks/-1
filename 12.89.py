sentence = input("Введите предложение: ")
if ',' in sentence:
    comma_pos = sentence.find(',')
    part_before_comma = sentence[:comma_pos]
    count_n = part_before_comma.count('н')
    print("Количество букв 'н' перед первой запятой:", count_n)
else:
    print("Запятых в предложении нет")