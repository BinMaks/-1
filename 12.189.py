sentence = input("Введите предложение: ")
words = sentence.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
duplicates = [word for word, count in word_count.items() if count == 2]
if duplicates:
    print("Повторяющееся слово:", duplicates[0])
else:
    print("Нет слов, повторяющихся ровно дважды.")