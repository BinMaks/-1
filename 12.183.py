sentence = input("Введите предложение: ")
words = sentence.split()
min_length = min(len(word) for word in words)
print("Длина самого короткого слова:", min_length)