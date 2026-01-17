sentence = input("Введите предложение (слова разделены одним пробелом): ")
words = sentence.split()
longest_word = max(words, key=len)
print("Самое длинное слово:", longest_word)