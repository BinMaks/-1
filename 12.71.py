
sentence = input("Введите предложение: ")
words = sentence.split()
if len(words) > 3:
    print("Число слов больше трех")
else:
    print("Число слов не больше трех")