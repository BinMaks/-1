sentence = input("Введите предложение: ")
total = len(sentence)
count_a = sentence.count('а')
percentage = (count_a / total) * 100
print("Доля букв 'а': {:.2f}%".format(percentage))