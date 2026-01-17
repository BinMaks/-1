sentence1 = input("Введите первое предложение: ").split()
sentence2 = input("Введите второе предложение: ").split()
all_words = sentence1 + sentence2
word_count = {}
for word in all_words:
    word_count[word] = word_count.get(word, 0) + 1
unique_words = [word for word, count in word_count.items() if count == 1]
print("Слова, встречающиеся только один раз:", unique_words)