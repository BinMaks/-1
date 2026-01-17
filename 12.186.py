sentence = input("Введите предложение: ")
words = sentence.split()
sorted_words = sorted(words, key=len)
print("Слова в порядке неубывания длины:", ' '.join(sorted_words))