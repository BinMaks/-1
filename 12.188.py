sentence = input("Введите предложение: ")
unique_words = set(sentence.split())
print("Различные слова:", ' '.join(sorted(unique_words)))