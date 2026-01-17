sentence = input("Введите предложение: ")
words = sentence.split()
if len(words) > 1:
    words[0], words[-1] = words[-1], words[0]
    print("После перестановки:", ' '.join(words))
else:
    print("Предложение содержит меньше двух слов.")