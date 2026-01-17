sentence = input("Введите предложение: ")
words = sentence.split()
longest_word = max(words, key=len)
print("Самое длинное слово:", longest_word)