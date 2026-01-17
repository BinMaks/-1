sentence = input("Введите предложение с запятыми: ")
comma_pos = sentence.find(',')
print(sentence[:comma_pos])