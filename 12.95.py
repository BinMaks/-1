sentence = input("Введите предложение: ")
pos_n = sentence.find('н')
pos_k = sentence.find('к')
if pos_n < pos_k:
    print("Буква 'н' встречается раньше")
elif pos_k < pos_n:
    print("Буква 'к' встречается раньше")
else:
    print("Буквы 'н' и 'к' встречаются на одинаковых позициях или отсутствуют")