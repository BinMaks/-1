sentence = input("Введите предложение: ")
count = sentence.count('ро')
print("Вхождений 'ро':", count)

sentence = input("Введите предложение: ")
combo = input("Введите буквосочетание из 2 букв: ")
count = sentence.count(combo)
print("Вхождений '{}': {}".format(combo, count))

sentence = input("Введите предложение: ")
combo = input("Введите буквосочетание: ")
count = sentence.count(combo)
print("Вхождений '{}': {}".format(combo, count))