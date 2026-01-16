
words = ["кот", "кошка", "собака", "конь", "крыса", "кролик", "кабан", "лиса", "волк", "тигр"]
avg_length = sum(len(word) for word in words) / len(words)
print("Средняя длина слова:", avg_length)
long_words = sum(1 for word in words if len(word) > 5)
print("Слов длиннее 5 символов:", long_words)
max_length = max(len(word) for word in words)
print("Длина самого длинного слова:", max_length)
min_length = min(len(word) for word in words)
shortest_word_index = next(i for i, word in enumerate(words) if len(word) == min_length)
print("Номер первого самого короткого слова:", shortest_word_index + 1)
second_longest_length = sorted(set(len(word) for word in words), reverse=True)[1]
print("Длина слова, больше которого только самое длинное:", second_longest_length)
k_words = sum(1 for word in words if word.lower().startswith('к'))
print("Слов, начинающихся на 'к' или 'К':", k_words)
sorted_words = sorted(words)
print("Слова в алфавитном порядке:", sorted_words)