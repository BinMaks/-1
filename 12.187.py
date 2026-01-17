sentence = input("Введите предложение: ")
words = sentence.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
unique_words = [word for word, count in word_count.items() if count == 1]
print("Слова, встречающиеся один раз:", ' '.join(unique_words))